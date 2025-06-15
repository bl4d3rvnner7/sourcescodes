import re, os

def clear_screen():
    if os.name == "nt":
        os.system('cls')
    else:
        os.system('clear')

def banner():
    print("""
\t██╗      ██████╗  ██████╗ ███████╗███████╗ █████╗ ██████╗  ██████╗██╗  ██╗
\t██║     ██╔═══██╗██╔════╝ ██╔════╝██╔════╝██╔══██╗██╔══██╗██╔════╝██║  ██║
\t██║     ██║   ██║██║  ███╗███████╗█████╗  ███████║██████╔╝██║     ███████║
\t██║     ██║   ██║██║   ██║╚════██║██╔══╝  ██╔══██║██╔══██╗██║     ██╔══██║
\t███████╗╚██████╔╝╚██████╔╝███████║███████╗██║  ██║██║  ██║╚██████╗██║  ██║
\t╚══════╝ ╚═════╝  ╚═════╝ ╚══════╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝
                                                                          
    """)
    

def remove_duplicates(file_path, output_file):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    unique_lines = sorted(set(lines))
    with open(output_file, 'w', encoding='utf-8') as file:
        file.writelines(unique_lines)
    print(f"Removed duplicates. Output saved to {output_file}.")

def remove_unknown(file_path, output_file):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    filtered_lines = [line for line in lines if "UNKNOWN" not in line]
    with open(output_file, 'w', encoding='utf-8') as file:
        file.writelines(filtered_lines)
    print(f"Removed 'UNKNOWN' entries. Output saved to {output_file}.")

def extract_urls(file_path, output_file):
    with open(file_path, 'r', encoding='utf-8') as file:
        logs = file.read()
    urls = re.findall(r'https?://[^\s<>"]+|www\.[^\s<>"]+', logs)
    unique_urls = sorted(set(urls))
    with open(output_file, 'w', encoding='utf-8') as file:
        file.writelines(f"{url}\n" for url in unique_urls)
    print(f"Extracted URLs. Output saved to {output_file}.")

def logs_to_combo(file_path, output_file):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    combos = [line.strip() for line in lines if ':' in line]
    with open(output_file, 'w', encoding='utf-8') as file:
        file.writelines(f"{combo}\n" for combo in combos)
    print(f"Converted logs to combo format. Output saved to {output_file}.")

def extract_pattern(file_path, pattern, output_file=None, domain_filter=None):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()

        results = []
        for line in lines:
            matches = re.findall(pattern, line)
            if matches:
                for match in matches:
                    if domain_filter:
                        if domain_filter in match:
                            results.append(match)
                    else:
                        results.append(match)

        if results:
            if output_file:
                with open(output_file, 'w', encoding='utf-8') as out_file:
                    out_file.write('\n'.join(results))
                print(f"Extracted data saved to {output_file}")
            else:
                print("\n".join(results))
        else:
            print("No matching data found.")

    except FileNotFoundError:
        print(f"File not found: {file_path}")
    except Exception as e:
        print(f"An error occurred: {e}")

def about_us():
    print("\nAbout Us:")
    print("Tool created for managing logs efficiently.")
    print("For assistance, contact @scarlettaowner.")

def main():
    clear_screen()
    banner()
    while True:
        print("\nMenu:")
        print("1 - Remove Duplicates from Logs")
        print("2 - Remove 'UNKNOWN' from Logs")
        print("3 - Extract URLs from Logs")
        print("4 - Logs to COMBO")
        print("5 - Extract Specific Patterns")
        print("6 - About Us")
        print("0 - Exit")

        choice = input("Select an option: ").strip()

        if choice == '1':
            file_path = input("Enter the log file path: ").strip()
            output_file = input("Enter the output file path: ").strip()
            remove_duplicates(file_path, output_file)
        elif choice == '2':
            file_path = input("Enter the log file path: ").strip()
            output_file = input("Enter the output file path: ").strip()
            remove_unknown(file_path, output_file)
        elif choice == '3':
            file_path = input("Enter the log file path: ").strip()
            output_file = input("Enter the output file path: ").strip()
            extract_urls(file_path, output_file)
        elif choice == '4':
            file_path = input("Enter the log file path: ").strip()
            output_file = input("Enter the output file path: ").strip()
            logs_to_combo(file_path, output_file)
        elif choice == '5':
            file_path = input("Enter the log file path: ").strip()
            if not file_path:
                print("Log file path is required. Please try again.")
                continue

            output_file = input("Enter the output file path: ").strip()
            if not output_file:
                print("Output file path is required. Please try again.")
                continue

            domain_filter = input("Enter domain filter (optional, e.g., example.com): ").strip() or None

            # The regex pattern is predefined for this case (URLs)
            pattern = r"https?://[^\s]+"  # Modify the pattern if needed

            print(f"Processing file: {file_path}")
            extract_pattern(file_path, pattern, output_file, domain_filter)

        elif choice == '6':
            about_us()
        elif choice == '0':
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()