import requests
import socks
import socket
import time
import random
from threading import Thread
from queue import Queue

# Queue for thread-safe proxy processing
proxy_queue = Queue()

def load_proxies(file_path):
    """Load proxies from file (host:port or host:port:user:pass)."""
    proxies = []
    try:
        with open(file_path, 'r') as f:
            for line in f:
                line = line.strip()
                if line:
                    parts = line.split(':')
                    if len(parts) >= 2:
                        proxy = {'host': parts[0], 'port': parts[1], 'user': None, 'pass': None}
                        if len(parts) == 4:
                            proxy['user'], proxy['pass'] = parts[2], parts[3]
                        proxies.append(proxy)
    except FileNotFoundError:
        print(f"Proxies file {file_path} not found. Check the path.")
        exit(1)
    return proxies

def test_proxy(proxy, timeout=5, test_url='http://ipinfo.io/ip'):
    """Test if SOCKS5 proxy is alive."""
    proxy_url = f"socks5://{proxy['user']}:{proxy['pass']}@{proxy['host']}:{proxy['port']}" if proxy['user'] else f"socks5://{proxy['host']}:{proxy['port']}"
    try:
        # Set up proxy
        socks.set_default_proxy(
            socks.SOCKS5, proxy['host'], int(proxy['port']),
            username=proxy['user'], password=proxy['pass']
        )
        socket.socket = socks.socksocket

        # Test connection
        start_time = time.time()
        response = requests.get(test_url, proxies={'http': proxy_url, 'https': proxy_url}, timeout=timeout)
        elapsed = time.time() - start_time

        if response.status_code == 200:
            return "alive", elapsed, None
        return "dead", None, f"HTTP {response.status_code}"
    except Exception as e:
        return "dead", None, str(e)
    finally:
        # Reset socket
        socket.socket = socket._socket.socket

def worker(proxy_queue, results, timeout, test_url):
    """Worker thread to process proxies."""
    while not proxy_queue.empty():
        proxy = proxy_queue.get()
        status, elapsed, error = test_proxy(proxy, timeout, test_url)
        proxy_str = f"{proxy['host']}:{proxy['port']}" + (f":{proxy['user']}:{proxy['pass']}" if proxy['user'] else "")
        results.append((proxy_str, status, elapsed, error))
        print(f"{proxy_str} -> {status.upper()}{' (' + str(round(elapsed, 2)) + 's)' if elapsed else ' (' + error + ')'}")
        # Random delay to avoid rate limits
        time.sleep(random.uniform(0.5, 1.5))
        proxy_queue.task_done()

def save_results(results):
    """Save results to files."""
    working_file = open("working_proxies.txt", "a")
    dead_file = open("dead_proxies.txt", "a")
    
    for proxy_str, status, elapsed, error in results:
        if status == "alive":
            working_file.write(f"{proxy_str} ({round(elapsed, 2)}s)\n")
        else:
            dead_file.write(f"{proxy_str} ({error})\n")
    
    working_file.close()
    dead_file.close()

def main(proxy_file, threads=10, timeout=5, test_url='http://ipinfo.io/ip'):
    """Main function to check proxies."""
    # Load proxies
    proxies = load_proxies(proxy_file)
    
    # Fill queue
    for proxy in proxies:
        proxy_queue.put(proxy)
    
    # Run workers
    results = []
    thread_list = []
    for _ in range(min(threads, len(proxies))):
        t = Thread(target=worker, args=(proxy_queue, results, timeout, test_url))
        t.start()
        thread_list.append(t)
    
    # Wait for all threads to finish
    for t in thread_list:
        t.join()
    
    # Save results
    save_results(results)
    
    # Summary
    alive_count = sum(1 for r in results if r[1] == "alive")
    dead_count = sum(1 for r in results if r[1] == "dead")
    print("\n=== Summary ===")
    print(f"Alive: {alive_count}")
    print(f"Dead: {dead_count}")
    print("Results saved to working_proxies.txt, dead_proxies.txt")

if __name__ == "__main__":
    proxy_file = "proxies.txt"
    threads = 10  # Adjust based on your setup
    timeout = 5  # Seconds for each proxy test
    test_url = "http://ipinfo.io/ip"  # Test endpoint
    main(proxy_file, threads, timeout, test_url)