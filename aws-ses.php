<?php
/**
 * W3LL Cyber Security Mailer v3.2
 * Samurai Edition - Advanced Mass Email System
 * Enhanced with LeafMailer-style functionality + Checker Integration
 */

$APP_PASSWORD = "W3LLSTORE";
session_start();
error_reporting(0);
set_time_limit(0);
ini_set("memory_limit", -1);
$SESSION_KEY = md5(__FILE__);

if (!empty($APP_PASSWORD) && $_SESSION[$SESSION_KEY] != $APP_PASSWORD) {
    if (isset($_REQUEST['pass']) && $_REQUEST['pass'] == $APP_PASSWORD) {
        $_SESSION[$SESSION_KEY] = $APP_PASSWORD;
    } else {
        print "<pre align=center><form method=post>Password: <input type='password' name='pass'><input type='submit' value='>>'></form></pre>";
        exit();
    }
}

function sanitizeInput($input) {
    return stripslashes(ltrim(rtrim($input)));
}

function processDynamicContent($content, $email) {
    $username = preg_replace('/([^@]*).*/', '$1', $email);
    $content = str_replace("[-time-]", date("m/d/Y h:i:s a", time()), $content);
    $content = str_replace("[-email-]", $email, $content);
    $content = str_replace("[-emailuser-]", $username, $content);
    $content = str_replace(
        "[-randomletters-]",
        generateRandomString('abcdefghijklmnopqrstuvwxyz'),
        $content
    );
    $content = str_replace(
        "[-randomstring-]",
        generateRandomString('abcdefghijklmnopqrstuvwxyz0123456789'),
        $content
    );
    $content = str_replace("[-randomnumber-]", generateRandomString('0123456789'), $content);
    $content = str_replace(
        "[-randommd5-]",
        md5(generateRandomString('abcdefghijklmnopqrstuvwxyz0123456789')),
        $content
    );
    return $content;
}

function generateRandomString($characters, $length = null) {
    $length = $length ?? rand(12, 25);
    $result = '';
    for ($i = 0; $i < $length; $i++) {
        $result .= $characters[rand() % strlen($characters)];
    }
    return $result;
}

function validateEmail($email) {
    $pattern = "^[a-z\'0-9]+([._-][a-z\'0-9]+)*@([a-z0-9]+([._-][a-z0-9]+))+$";
    if (preg_match("/$pattern/i", $email)) {
        $domain = explode("@", $email)[1];
        return checkdnsrr($domain, "MX");
    }
    return false;
}

class W3LLMailer {
    public $smtpHost = 'localhost';
    public $smtpPort = 587;
    public $smtpAuth = false;
    public $smtpUsername = '';
    public $smtpPassword = '';
    public $smtpEncryption = 'tls';
    public $fromEmail = '';
    public $fromName = '';
    public $replyTo = '';
    public $subject = '';
    public $isHtml = true;
    public $charset = 'UTF-8';
    public $errorInfo = '';
    public $mailerType = 'mail';
    
    private $recipients = array();
    private $messageBody = '';
    
    public function isSMTP() {
        $this->mailerType = 'smtp';
    }
    
    public function isMail() {
        $this->mailerType = 'mail';
    }
    
    public function addAddress($email, $name = '') {
        $this->recipients[] = array($email, $name);
    }
    
    public function setFrom($email, $name = '') {
        $this->fromEmail = $email;
        $this->fromName = $name;
    }
    
    public function addReplyTo($email) {
        $this->replyTo = $email;
    }
    
    public function isHTML($isHtml = true) {
        $this->isHtml = $isHtml;
    }
    
    public function send() {
        if ($this->mailerType == 'smtp') {
            return $this->sendSMTP();
        } else {
            return $this->sendMail();
        }
    }
    
    private function sendSMTP() {
        if (empty($this->recipients)) {
            return false;
        }
        
        $recipientEmail = $this->recipients[0][0];
        $context = stream_context_create();
        $hostname = $this->smtpHost;
        
        if ($this->smtpEncryption == 'ssl') {
            $hostname = 'ssl://' . $hostname;
        }
        
        $socket = @fsockopen($hostname, $this->smtpPort, $errno, $errstr, 30);
        if (!$socket) {
            $this->errorInfo = "Could not connect to SMTP host: $errstr ($errno)";
            return false;
        }
        
        $response = fgets($socket, 515);
        if (substr($response, 0, 3) != '220') {
            $this->errorInfo = "SMTP Error: $response";
            fclose($socket);
            return false;
        }
        
        fputs($socket, "EHLO " . ($_SERVER['HTTP_HOST'] ?? 'localhost') . "\r\n");
        $response = fgets($socket, 515);
        
        if ($this->smtpEncryption == 'tls') {
            fputs($socket, "STARTTLS\r\n");
            $response = fgets($socket, 515);
            if (substr($response, 0, 3) != '220') {
                $this->errorInfo = "STARTTLS failed: $response";
                fclose($socket);
                return false;
            }
            
            if (!stream_socket_enable_crypto($socket, true, STREAM_CRYPTO_METHOD_TLS_CLIENT)) {
                $this->errorInfo = "TLS encryption failed";
                fclose($socket);
                return false;
            }
            
            fputs($socket, "EHLO " . ($_SERVER['HTTP_HOST'] ?? 'localhost') . "\r\n");
            $response = fgets($socket, 515);
        }
        
        if ($this->smtpAuth) {
            fputs($socket, "AUTH LOGIN\r\n");
            $response = fgets($socket, 515);
            if (substr($response, 0, 3) != '334') {
                $this->errorInfo = "AUTH LOGIN failed: $response";
                fclose($socket);
                return false;
            }
            
            fputs($socket, base64_encode($this->smtpUsername) . "\r\n");
            $response = fgets($socket, 515);
            if (substr($response, 0, 3) != '334') {
                $this->errorInfo = "Username authentication failed: $response";
                fclose($socket);
                return false;
            }
            
            fputs($socket, base64_encode($this->smtpPassword) . "\r\n");
            $response = fgets($socket, 515);
            if (substr($response, 0, 3) != '235') {
                $this->errorInfo = "Password authentication failed: $response";
                fclose($socket);
                return false;
            }
        }
        
        fputs($socket, "MAIL FROM: <{$this->fromEmail}>\r\n");
        $response = fgets($socket, 515);
        if (substr($response, 0, 3) != '250') {
            $this->errorInfo = "MAIL FROM failed: $response";
            fclose($socket);
            return false;
        }
        
        fputs($socket, "RCPT TO: <$recipientEmail>\r\n");
        $response = fgets($socket, 515);
        if (substr($response, 0, 3) != '250') {
            $this->errorInfo = "RCPT TO failed: $response";
            fclose($socket);
            return false;
        }
        
        fputs($socket, "DATA\r\n");
        $response = fgets($socket, 515);
        if (substr($response, 0, 3) != '354') {
            $this->errorInfo = "DATA command failed: $response";
            fclose($socket);
            return false;
        }
        
        $headers = "MIME-Version: 1.0\r\n";
        $headers .= "Content-Type: " . ($this->isHtml ? 'text/html' : 'text/plain') . "; charset={$this->charset}\r\n";
        $headers .= "From: {$this->fromName} <{$this->fromEmail}>\r\n";
        $headers .= "To: $recipientEmail\r\n";
        
        if ($this->replyTo) {
            $headers .= "Reply-To: {$this->replyTo}\r\n";
        }
        
        $headers .= "Subject: {$this->subject}\r\n";
        $headers .= "X-Mailer: W3LL Cyber Samurai Mailer 3.2\r\n";
        $headers .= "Date: " . date('r') . "\r\n";
        $headers .= "\r\n";
        
        fputs($socket, $headers . $this->messageBody . "\r\n.\r\n");
        $response = fgets($socket, 515);
        fputs($socket, "QUIT\r\n");
        fclose($socket);
        
        if (substr($response, 0, 3) != '250') {
            $this->errorInfo = "Message sending failed: $response";
            return false;
        }
        
        return true;
    }
    
    private function sendMail() {
        if (empty($this->recipients)) {
            return false;
        }
        
        $recipientEmail = $this->recipients[0][0];
        $headers = array();
        $headers[] = 'MIME-Version: 1.0';
        $headers[] = 'Content-Type: ' . ($this->isHtml ? 'text/html' : 'text/plain') . '; charset=' . $this->charset;
        $headers[] = 'From: ' . $this->fromName . ' <' . $this->fromEmail . '>';
        
        if ($this->replyTo) {
            $headers[] = 'Reply-To: ' . $this->replyTo;
        }
        
        $headers[] = 'X-Mailer: W3LL Cyber Samurai Mailer 3.2';
        $headers[] = 'Date: ' . date('r');
        
        $result = @mail($recipientEmail, $this->subject, $this->messageBody, implode("\r\n", $headers));
        
        if (!$result) {
            $this->errorInfo = "PHP mail() function failed";
            return false;
        }
        
        return true;
    }
    
    public function clearAddresses() {
        $this->recipients = array();
    }
}

// Process form submission
if ($_POST['action'] == "send") {
    $senderEmail = sanitizeInput($_POST['senderEmail']);
    $senderName = sanitizeInput($_POST['senderName']);
    $replyTo = sanitizeInput($_POST['replyTo']);
    $subject = sanitizeInput($_POST['subject']);
    $emailList = sanitizeInput($_POST['emailList']);
    $messageType = sanitizeInput($_POST['messageType']);
    $messageContent = sanitizeInput($_POST['messageLetter']);
    $useSmtp = $_POST['useSmtp'] ?? 0;
    $smtpHost = sanitizeInput($_POST['smtpHost']);
    $smtpPort = sanitizeInput($_POST['smtpPort']) ?: 587;
    $smtpEmail = sanitizeInput($_POST['smtpEmail']);
    $smtpPassword = sanitizeInput($_POST['smtpPassword']);
    $smtpEncryption = sanitizeInput($_POST['smtpEncryption']);
    
    $messageContent = urlencode($messageContent);
    $messageContent = preg_replace("/%5C%22/", "%22", $messageContent);
    $messageContent = urldecode($messageContent);
    $messageContent = stripslashes($messageContent);
    $subject = stripslashes($subject);
}

// Set default values for form
$messageType = $_POST['messageType'] ?? 1;
if ($messageType == 2) {
    $isTextChecked = "checked";
    $isHtmlChecked = "";
} else {
    $isHtmlChecked = "checked";
    $isTextChecked = "";
}

$senderEmail = $_POST['senderEmail'] ?? '';
$senderName = $_POST['senderName'] ?? '';
$replyTo = $_POST['replyTo'] ?? '';
$subject = $_POST['subject'] ?? '';
$emailList = $_POST['emailList'] ?? '';
$messageContent = $_POST['messageLetter'] ?? '';
$useSmtp = $_POST['useSmtp'] ?? 0;
$smtpHost = $_POST['smtpHost'] ?? '';
$smtpPort = $_POST['smtpPort'] ?? 587;
$smtpEmail = $_POST['smtpEmail'] ?? '';
$smtpPassword = $_POST['smtpPassword'] ?? '';
$smtpEncryption = $_POST['smtpEncryption'] ?? 'tls';

// API endpoints for validation and testing
if (isset($_GET['valid'])) {
    $responseData = array(
        'info' => true,
        'zip' => function_exists('zip_open') || class_exists('ZipArchive'),
        'delivery' => function_exists('mail') && ini_get('sendmail_path'),
        'mailer_type' => 'W3LL Cyber Samurai Mailer',
        'version' => '3.2 Enhanced Edition',
        'capabilities' => array(
            'smtp' => function_exists('fsockopen'),
            'mail' => function_exists('mail'),
            'ssl' => extension_loaded('openssl'),
            'mass_email' => true,
            'dynamic_content' => true
        ),
        'server_info' => array(
            'php_version' => phpversion(),
            'server_software' => $_SERVER['SERVER_SOFTWARE'] ?? 'Unknown',
            'document_root' => $_SERVER['DOCUMENT_ROOT'] ?? 'Unknown',
            'server_ip' => $_SERVER['SERVER_ADDR'] ?? gethostbyname(gethostname()),
            'host' => $_SERVER['HTTP_HOST'] ?? 'Unknown'
        ),
        'w3ll_signature' => 'W3LL_CYBER_SAMURAI_VERIFIED',
        'status' => 'active',
        'timestamp' => date('Y-m-d H:i:s')
    );
    
    if (isset($_GET['email']) && isset($_GET['id'])) {
        $email = $_GET['email'];
        $id = $_GET['id'];
        $logEntry = date('Y-m-d H:i:s') . " - W3LL Checker Validation - Email: $email - ID: $id\n";
        @file_put_contents('w3ll_checker_logs.txt', $logEntry, FILE_APPEND | LOCK_EX);
    }
    
    header('Content-Type: application/json');
    echo json_encode($responseData);
    exit();
}

// Test email endpoint
if (isset($_GET['send_test_email']) || isset($_GET['test']) || isset($_GET['delivery'])) {
    $email = $_GET['email'] ?? '';
    $id = $_GET['id'] ?? '';
    $logEntry = date('Y-m-d H:i:s') . " - Checker Email Test - Email: $email - ID: $id\n";
    @file_put_contents('w3ll_checker_logs.txt', $logEntry, FILE_APPEND | LOCK_EX);
    
    if (empty($email) || !filter_var($email, FILTER_VALIDATE_EMAIL)) {
        header('Content-Type: application/json');
        echo json_encode([
            'status' => 'error',
            'message' => 'Invalid email format',
            'email_sent' => false,
            'error' => 'Email validation failed'
        ]);
        exit();
    }
    
    try {
        $mailer = new W3LLMailer();
        $mailer->isMail();
        $mailer->setFrom('noreply@' . ($_SERVER['HTTP_HOST'] ?? 'localhost'), 'W3LL Mailer Test');
        $mailer->addAddress($email);
        $mailer->subject = 'W3LL Cyber Samurai Mailer Test - ID: ' . $id;
        $mailer->messageBody = "This is a test email from W3LL Cyber Samurai Mailer.\n\nTimestamp: " . 
                              date('Y-m-d H:i:s') . 
                              "\nProduct ID: " . $id . 
                              "\nMailer Version: 3.2 Enhanced Edition\n\nThis confirms that the mailer is working properly.";
        $mailer->isHTML(false);
        
        if ($mailer->send()) {
            header('Content-Type: application/json');
            echo json_encode([
                'status' => 'ok',
                'email_sent' => true,
                'message' => 'success',
                'delivered' => true,
                'sent' => true,
                'timestamp' => date('Y-m-d H:i:s'),
                'mailer_type' => 'W3LL Cyber Samurai Mailer',
                'version' => '3.2 Enhanced Edition',
                'w3ll_signature' => 'W3LL_CYBER_SAMURAI_VERIFIED'
            ]);
        } else {
            header('Content-Type: application/json');
            echo json_encode([
                'status' => 'error',
                'email_sent' => false,
                'message' => 'failed to send',
                'error' => $mailer->errorInfo ?: 'Unknown error occurred'
            ]);
        }
    } catch (Exception $e) {
        header('Content-Type: application/json');
        echo json_encode([
            'status' => 'error',
            'email_sent' => false,
            'message' => 'exception occurred',
            'error' => $e->getMessage()
        ]);
    }
    exit();
}

// Capability check endpoint
if (isset($_GET['check_capability'])) {
    header('Content-Type: application/json');
    echo json_encode([
        'mailer_detected' => true,
        'type' => 'W3LL Cyber Samurai Mailer',
        'version' => '3.2 Enhanced Edition',
        'capabilities' => [
            'smtp' => function_exists('fsockopen'),
            'mail' => function_exists('mail'),
            'ssl' => extension_loaded('openssl'),
            'mass_email' => true,
            'html_email' => true,
            'dynamic_variables' => true
        ],
        'status' => 'working',
        'w3ll_signature' => 'W3LL_CYBER_SAMURAI_VERIFIED'
    ]);
    exit();
}

// Health check endpoint
if (isset($_GET['health']) || isset($_GET['status'])) {
    header('Content-Type: application/json');
    echo json_encode([
        'status' => 'healthy',
        'mailer' => 'W3LL Cyber Samurai Mailer',
        'version' => '3.2 Enhanced Edition',
        'uptime' => true,
        'mail_function' => function_exists('mail'),
        'smtp_support' => function_exists('fsockopen'),
        'timestamp' => date('Y-m-d H:i:s'),
        'w3ll_signature' => 'W3LL_CYBER_SAMURAI_VERIFIED'
    ]);
    exit();
}
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>W3LL 侍 Cyber Samurai Mailer | Advanced Mass Email System</title>
    <meta name="description" content="Advanced Mass Email System by W3LL Store - Enhanced with LeafMailer functionality + Checker Integration">
    <link href="https://fonts.googleapis.com/css2?family=Orbitron:wght@400;500;700;900&family=Inter:wght@300;400;500;600&family=Noto+Sans+JP:wght@300;400;500;700&family=Fira+Code:wght@300;400;500;600&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    
    <style>
        :root {
            --cyber-primary: #00ff88;
            --cyber-secondary: #ff0080;
            --cyber-tertiary: #0080ff;
            --cyber-quaternary: #8000ff;
            --cyber-gold: #ffd700;
            --cyber-red: #ff3333;
            --cyber-orange: #ff8800;
            
            --dark-primary: #0a0a0a;
            --dark-secondary: #1a1a2e;
            --dark-tertiary: #16213e;
            --dark-quaternary: #0f3460;
            
            --text-primary: #ffffff;
            --text-secondary: #b0b0b0;
            --text-tertiary: #808080;
            
            --gradient-cyber: linear-gradient(135deg, var(--cyber-primary) 0%, var(--cyber-tertiary) 50%, var(--cyber-quaternary) 100%);
            --gradient-danger: linear-gradient(135deg, var(--cyber-red) 0%, var(--cyber-secondary) 100%);
            --gradient-warning: linear-gradient(135deg, var(--cyber-orange) 0%, var(--cyber-gold) 100%);
            --gradient-dark: linear-gradient(135deg, var(--dark-primary) 0%, var(--dark-tertiary) 50%, var(--dark-quaternary) 100%);
            
            --shadow-cyber: 0 0 20px rgba(0, 255, 136, 0.3);
            --shadow-neon: 0 0 30px rgba(0, 255, 136, 0.5);
            --shadow-dark: 0 15px 35px rgba(0, 0, 0, 0.5);
        }

        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: 'Inter', 'Noto Sans JP', sans-serif;
            background: var(--gradient-dark);
            color: var(--text-primary);
            min-height: 100vh;
            position: relative;
            overflow-x: hidden;
        }

        /* Matrix Background Effect */
        .cyber-matrix {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            z-index: -2;
            opacity: 0.03;
        }

        /* Animated Grid Background */
        .cyber-grid {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background-image: 
                linear-gradient(rgba(0, 255, 136, 0.1) 1px, transparent 1px),
                linear-gradient(90deg, rgba(0, 255, 136, 0.1) 1px, transparent 1px);
            background-size: 50px 50px;
            z-index: -1;
            animation: gridMove 20s linear infinite;
        }

        @keyframes gridMove {
            0% { transform: translate(0, 0); }
            100% { transform: translate(50px, 50px); }
        }

        /* Header Styling */
        .cyber-header {
            background: rgba(26, 26, 46, 0.95);
            backdrop-filter: blur(15px);
            border-bottom: 2px solid var(--cyber-primary);
            padding: 1rem 0;
            position: sticky;
            top: 0;
            z-index: 1000;
            box-shadow: var(--shadow-cyber);
        }

        .header-content {
            max-width: 1400px;
            margin: 0 auto;
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 0 2rem;
        }

        .cyber-logo {
            display: flex;
            align-items: center;
            gap: 1rem;
            text-decoration: none;
            color: var(--text-primary);
            font-family: 'Orbitron', monospace;
            font-weight: 900;
            font-size: 1.5rem;
            text-shadow: 0 0 10px var(--cyber-primary);
            transition: all 0.3s ease;
        }

        .cyber-logo:hover {
            color: var(--cyber-primary);
            text-shadow: var(--shadow-neon);
            transform: scale(1.05);
        }

        .cyber-logo i {
            font-size: 2rem;
            color: var(--cyber-gold);
            animation: pulse 2s infinite;
        }

        .nav-links {
            display: flex;
            gap: 2rem;
        }

        .nav-link {
            color: var(--text-secondary);
            text-decoration: none;
            font-weight: 600;
            padding: 0.5rem 1rem;
            border: 1px solid transparent;
            border-radius: 8px;
            transition: all 0.3s ease;
            font-family: 'Orbitron', monospace;
            font-size: 0.9rem;
        }

        .nav-link:hover {
            color: var(--cyber-primary);
            border-color: var(--cyber-primary);
            box-shadow: var(--shadow-cyber);
            transform: translateY(-2px);
        }

        /* Container and Layout */
        .container {
            max-width: 1400px;
            margin: 0 auto;
            padding: 2rem;
        }

        .row {
            display: grid;
            grid-template-columns: 1fr 400px;
            gap: 2rem;
            margin-bottom: 2rem;
        }

        @media (max-width: 1200px) {
            .row {
                grid-template-columns: 1fr;
            }
        }

        /* Enhanced Card Styling */
        .cyber-card {
            background: rgba(26, 26, 46, 0.95);
            backdrop-filter: blur(15px);
            border: 2px solid rgba(0, 255, 136, 0.3);
            border-radius: 20px;
            overflow: hidden;
            box-shadow: var(--shadow-dark);
            transition: all 0.3s ease;
            position: relative;
        }

        .cyber-card::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            height: 2px;
            background: var(--gradient-cyber);
            animation: shimmer 3s ease-in-out infinite;
        }

        @keyframes shimmer {
            0%, 100% { opacity: 0.5; }
            50% { opacity: 1; }
        }

        .cyber-card:hover {
            border-color: var(--cyber-primary);
            box-shadow: var(--shadow-neon);
            transform: translateY(-5px);
        }

        .card-header {
            background: linear-gradient(135deg, rgba(0, 255, 136, 0.1) 0%, rgba(0, 128, 255, 0.1) 100%);
            padding: 1.5rem 2rem;
            border-bottom: 1px solid rgba(0, 255, 136, 0.2);
        }

        .card-title {
            font-family: 'Orbitron', monospace;
            font-weight: 900;
            font-size: 1.3rem;
            color: var(--text-primary);
            display: flex;
            align-items: center;
            gap: 1rem;
            text-shadow: 0 0 10px var(--cyber-primary);
        }

        .card-title i {
            color: var(--cyber-primary);
            font-size: 1.5rem;
            animation: pulse 2s infinite;
        }

        .card-body {
            padding: 2rem;
        }

        /* Enhanced Form Styling */
        .form-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 1.5rem;
            margin-bottom: 2rem;
        }

        .form-group {
            display: flex;
            flex-direction: column;
            gap: 0.5rem;
        }

        .form-label {
            font-family: 'Orbitron', monospace;
            font-weight: 600;
            color: var(--cyber-primary);
            display: flex;
            align-items: center;
            gap: 0.5rem;
            font-size: 0.9rem;
            text-transform: uppercase;
            letter-spacing: 1px;
        }

        .form-label i {
            color: var(--cyber-gold);
            font-size: 1rem;
        }

                /* Enhanced Input Styling */
                .cyber-input, .cyber-textarea, .cyber-select {
            background: rgba(0, 0, 0, 0.3);
            border: 2px solid rgba(0, 255, 136, 0.3);
            border-radius: 10px;
            padding: 1rem;
            color: var(--text-primary);
            font-family: 'Fira Code', monospace;
            font-size: 0.9rem;
            transition: all 0.3s ease;
            backdrop-filter: blur(10px);
        }

        .cyber-input:focus, .cyber-textarea:focus, .cyber-select:focus {
            outline: none;
            border-color: var(--cyber-primary);
            box-shadow: var(--shadow-cyber);
            background: rgba(0, 0, 0, 0.5);
        }

        .cyber-textarea {
            min-height: 150px;
            resize: vertical;
            font-family: 'Fira Code', monospace;
        }

        /* Enhanced Checkbox and Radio Styling */
        .cyber-checkbox {
            display: flex;
            align-items: center;
            gap: 1rem;
            margin-bottom: 1.5rem;
            padding: 1rem;
            background: rgba(0, 255, 136, 0.05);
            border: 1px solid rgba(0, 255, 136, 0.2);
            border-radius: 10px;
            transition: all 0.3s ease;
        }

        .cyber-checkbox:hover {
            background: rgba(0, 255, 136, 0.1);
            border-color: var(--cyber-primary);
        }

        .cyber-checkbox input[type="checkbox"] {
            width: 20px;
            height: 20px;
            accent-color: var(--cyber-primary);
        }

        .cyber-checkbox label {
            font-family: 'Orbitron', monospace;
            font-weight: 600;
            color: var(--text-primary);
            display: flex;
            align-items: center;
            gap: 0.5rem;
            cursor: pointer;
        }

        .radio-group {
            display: flex;
            gap: 2rem;
        }

        .cyber-radio {
            display: flex;
            align-items: center;
            gap: 0.5rem;
        }

        .cyber-radio input[type="radio"] {
            width: 18px;
            height: 18px;
            accent-color: var(--cyber-primary);
        }

        .cyber-radio label {
            font-family: 'Orbitron', monospace;
            font-weight: 600;
            color: var(--text-primary);
            cursor: pointer;
        }

        /* SMTP Panel Styling */
        .smtp-panel {
            background: rgba(0, 128, 255, 0.05);
            border: 2px solid rgba(0, 128, 255, 0.3);
            border-radius: 15px;
            padding: 2rem;
            margin: 1.5rem 0;
            transition: all 0.3s ease;
        }

        .smtp-panel:hover {
            border-color: var(--cyber-tertiary);
            box-shadow: 0 0 20px rgba(0, 128, 255, 0.3);
        }

        /* Enhanced Button Styling */
        .button-group {
            display: flex;
            gap: 1rem;
            flex-wrap: wrap;
            justify-content: center;
            margin-top: 2rem;
        }

        .cyber-btn {
            padding: 1rem 2rem;
            border: none;
            border-radius: 12px;
            font-family: 'Orbitron', monospace;
            font-weight: 700;
            font-size: 0.9rem;
            text-transform: uppercase;
            letter-spacing: 1px;
            cursor: pointer;
            transition: all 0.3s ease;
            display: flex;
            align-items: center;
            gap: 0.5rem;
            text-decoration: none;
            position: relative;
            overflow: hidden;
        }

        .cyber-btn::before {
            content: '';
            position: absolute;
            top: 0;
            left: -100%;
            width: 100%;
            height: 100%;
            background: linear-gradient(90deg, transparent, rgba(255, 255, 255, 0.2), transparent);
            transition: left 0.5s;
        }

        .cyber-btn:hover::before {
            left: 100%;
        }

        .btn-primary {
            background: var(--gradient-cyber);
            color: var(--dark-primary);
            box-shadow: var(--shadow-cyber);
        }

        .btn-primary:hover {
            transform: translateY(-3px);
            box-shadow: var(--shadow-neon);
        }

        .btn-secondary {
            background: rgba(0, 128, 255, 0.2);
            color: var(--cyber-tertiary);
            border: 2px solid var(--cyber-tertiary);
        }

        .btn-secondary:hover {
            background: var(--cyber-tertiary);
            color: var(--dark-primary);
            transform: translateY(-3px);
        }

        .btn-danger {
            background: var(--gradient-danger);
            color: var(--text-primary);
        }

        .btn-danger:hover {
            transform: translateY(-3px);
            box-shadow: 0 0 30px rgba(255, 51, 51, 0.5);
        }

        /* Instructions Panel Styling */
        .instructions-panel {
            background: rgba(0, 0, 0, 0.3);
            border: 1px solid rgba(0, 255, 136, 0.2);
            border-radius: 12px;
            padding: 1.5rem;
            margin-bottom: 1.5rem;
            backdrop-filter: blur(10px);
        }

        .instructions-title {
            font-family: 'Orbitron', monospace;
            font-weight: 700;
            color: var(--cyber-primary);
            display: flex;
            align-items: center;
            gap: 0.5rem;
            margin-bottom: 1rem;
            font-size: 1rem;
            text-transform: uppercase;
            letter-spacing: 1px;
        }

        .instructions-title i {
            color: var(--cyber-gold);
        }

        .variable-list {
            list-style: none;
            padding: 0;
        }

        .variable-list li {
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 0.8rem;
            margin-bottom: 0.5rem;
            background: rgba(0, 255, 136, 0.05);
            border: 1px solid rgba(0, 255, 136, 0.1);
            border-radius: 8px;
            transition: all 0.3s ease;
        }

        .variable-list li:hover {
            background: rgba(0, 255, 136, 0.1);
            border-color: var(--cyber-primary);
            transform: translateX(5px);
        }

        .variable-code {
            font-family: 'Fira Code', monospace;
            background: rgba(0, 0, 0, 0.5);
            color: var(--cyber-gold);
            padding: 0.3rem 0.6rem;
            border-radius: 6px;
            font-weight: 600;
            border: 1px solid rgba(255, 215, 0, 0.3);
        }

        .status-success {
            color: var(--cyber-primary);
            font-weight: 600;
        }

        .status-danger {
            color: var(--cyber-red);
            font-weight: 600;
        }

        /* Results Display Styling */
        .results-panel {
            background: rgba(0, 0, 0, 0.4);
            border-radius: 15px;
            overflow: hidden;
        }

        .results-header {
            background: var(--gradient-cyber);
            color: var(--dark-primary);
            padding: 1rem 2rem;
            font-family: 'Orbitron', monospace;
            font-weight: 700;
            display: flex;
            align-items: center;
            gap: 1rem;
            text-transform: uppercase;
            letter-spacing: 1px;
        }

        .results-body {
            padding: 2rem;
            max-height: 600px;
            overflow-y: auto;
        }

        /* Custom Scrollbar */
        .results-body::-webkit-scrollbar {
            width: 8px;
        }

        .results-body::-webkit-scrollbar-track {
            background: rgba(0, 0, 0, 0.3);
            border-radius: 4px;
        }

        .results-body::-webkit-scrollbar-thumb {
            background: var(--gradient-cyber);
            border-radius: 4px;
        }

        .results-body::-webkit-scrollbar-thumb:hover {
            background: var(--cyber-primary);
        }

        /* Mass Results Styling */
        .mass-results {
            font-family: 'Fira Code', monospace;
            font-size: 0.9rem;
            line-height: 1.6;
        }

        .email-row {
            display: grid;
            grid-template-columns: 100px 1fr 120px;
            gap: 1rem;
            padding: 0.8rem 0;
            border-bottom: 1px solid rgba(0, 255, 136, 0.1);
            align-items: center;
            transition: all 0.3s ease;
        }

        .email-row:hover {
            background: rgba(0, 255, 136, 0.05);
            padding-left: 1rem;
            border-radius: 8px;
        }

        .email-counter {
            color: var(--cyber-gold);
            font-weight: bold;
            font-family: 'Orbitron', monospace;
            text-align: center;
            background: rgba(255, 215, 0, 0.1);
            padding: 0.3rem;
            border-radius: 6px;
            border: 1px solid rgba(255, 215, 0, 0.3);
        }

        .email-address {
            color: var(--text-primary);
            word-break: break-all;
            font-family: 'Fira Code', monospace;
        }

        .email-status {
            text-align: right;
        }

        .status-badge {
            padding: 0.4rem 1rem;
            border-radius: 20px;
            font-size: 0.8rem;
            font-weight: 700;
            text-transform: uppercase;
            letter-spacing: 0.5px;
            font-family: 'Orbitron', monospace;
            display: inline-flex;
            align-items: center;
            gap: 0.3rem;
        }

        .status-ok {
            background: rgba(0, 255, 136, 0.2);
            color: var(--cyber-primary);
            border: 1px solid var(--cyber-primary);
            box-shadow: 0 0 10px rgba(0, 255, 136, 0.3);
        }

        .status-ok::before {
            content: '✓';
        }

        .status-fail {
            background: rgba(255, 51, 51, 0.2);
            color: var(--cyber-red);
            border: 1px solid var(--cyber-red);
            box-shadow: 0 0 10px rgba(255, 51, 51, 0.3);
        }

        .status-fail::before {
            content: '✗';
        }

        .status-invalid {
            background: rgba(255, 136, 0, 0.2);
            color: var(--cyber-orange);
            border: 1px solid var(--cyber-orange);
            box-shadow: 0 0 10px rgba(255, 136, 0, 0.3);
        }

        .status-invalid::before {
            content: '⚠';
        }

        /* Progress Bar Styling */
        .progress-bar {
            width: 100%;
            height: 6px;
            background: rgba(0, 0, 0, 0.5);
            border-radius: 3px;
            overflow: hidden;
            margin: 1.5rem 0;
            border: 1px solid rgba(0, 255, 136, 0.3);
        }

        .progress-fill {
            height: 100%;
            background: var(--gradient-cyber);
            width: 0%;
            transition: width 0.5s ease;
            border-radius: 3px;
            position: relative;
            overflow: hidden;
        }

        .progress-fill::after {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            bottom: 0;
            right: 0;
            background-image: linear-gradient(
                -45deg,
                rgba(255, 255, 255, 0.2) 25%,
                transparent 25%,
                transparent 50%,
                rgba(255, 255, 255, 0.2) 50%,
                rgba(255, 255, 255, 0.2) 75%,
                transparent 75%,
                transparent
            );
            background-size: 50px 50px;
            animation: move 2s linear infinite;
        }

        @keyframes move {
            0% { background-position: 0 0; }
            100% { background-position: 50px 50px; }
        }

        /* Loading Spinner */
        .loading-spinner {
            width: 20px;
            height: 20px;
            border: 2px solid rgba(0, 255, 136, 0.3);
            border-radius: 50%;
            border-top-color: var(--cyber-primary);
            animation: spin 1s ease-in-out infinite;
        }

        @keyframes spin {
            to { transform: rotate(360deg); }
        }

        /* Footer Styling */
        .cyber-footer {
            background: rgba(26, 26, 46, 0.95);
            backdrop-filter: blur(15px);
            border-top: 2px solid var(--cyber-primary);
            padding: 2rem 0;
            margin-top: 4rem;
            text-align: center;
        }

        .footer-content {
            max-width: 1400px;
            margin: 0 auto;
            padding: 0 2rem;
        }

        .footer-links {
            display: flex;
            justify-content: center;
            gap: 2rem;
            margin-bottom: 2rem;
            flex-wrap: wrap;
        }

        .footer-link {
            color: var(--text-secondary);
            text-decoration: none;
            font-family: 'Orbitron', monospace;
            font-weight: 600;
            padding: 0.8rem 1.5rem;
            border: 1px solid rgba(0, 255, 136, 0.3);
            border-radius: 10px;
            transition: all 0.3s ease;
            display: flex;
            align-items: center;
            gap: 0.5rem;
        }

        .footer-link:hover {
            color: var(--cyber-primary);
            border-color: var(--cyber-primary);
            box-shadow: var(--shadow-cyber);
            transform: translateY(-3px);
        }

        .copyright {
            color: var(--text-tertiary);
            font-size: 0.9rem;
            line-height: 1.6;
        }

        .copyright p:first-child {
            font-family: 'Orbitron', monospace;
            font-weight: 600;
            color: var(--text-secondary);
            margin-bottom: 0.5rem;
        }

        /* Pulse Animation */
        @keyframes pulse {
            0%, 100% { 
                opacity: 1; 
                transform: scale(1);
            }
            50% { 
                opacity: 0.7; 
                transform: scale(1.05);
            }
        }

        /* Glow Animation */
        @keyframes glow {
            0%, 100% { 
                text-shadow: 0 0 5px var(--cyber-primary);
            }
            50% { 
                text-shadow: 0 0 20px var(--cyber-primary), 0 0 30px var(--cyber-primary);
            }
        }

        /* Responsive Design */
        @media (max-width: 768px) {
            .header-content {
                flex-direction: column;
                gap: 1rem;
                text-align: center;
            }

            .nav-links {
                flex-wrap: wrap;
                justify-content: center;
            }

            .container {
                padding: 1rem;
            }

            .form-grid {
                grid-template-columns: 1fr;
            }

            .button-group {
                flex-direction: column;
                align-items: center;
            }

            .cyber-btn {
                width: 100%;
                max-width: 300px;
                justify-content: center;
            }

            .email-row {
                grid-template-columns: 80px 1fr 100px;
                gap: 0.5rem;
                font-size: 0.8rem;
            }

            .footer-links {
                flex-direction: column;
                align-items: center;
            }
        }

        /* Japanese Text Styling */
        .japanese-text {
            font-family: 'Noto Sans JP', sans-serif;
            font-weight: 400;
        }

        /* Cyber Glitch Effect */
        .glitch {
            position: relative;
            animation: glitch 2s infinite;
        }

        @keyframes glitch {
            0%, 100% { transform: translate(0); }
            20% { transform: translate(-2px, 2px); }
            40% { transform: translate(-2px, -2px); }
            60% { transform: translate(2px, 2px); }
            80% { transform: translate(2px, -2px); }
        }

        /* Notification Styling */
        .notification {
            position: fixed;
            top: 100px;
            right: 20px;
            background: rgba(26, 26, 46, 0.95);
            backdrop-filter: blur(15px);
            padding: 1rem 2rem;
            border-radius: 15px;
            border: 2px solid var(--cyber-primary);
            z-index: 10000;
            box-shadow: var(--shadow-neon);
            font-family: 'Orbitron', monospace;
            font-weight: 600;
            animation: slideInRight 0.5s ease;
            max-width: 400px;
            display: flex;
            align-items: center;
            gap: 1rem;
        }

        @keyframes slideInRight {
            from { 
                transform: translateX(100%); 
                opacity: 0; 
            }
            to { 
                transform: translateX(0); 
                opacity: 1; 
            }
        }

        /* Enhanced Hover Effects */
        .cyber-card:hover .card-title {
            animation: glow 2s infinite;
        }

        .cyber-input:focus::placeholder,
        .cyber-textarea:focus::placeholder {
            color: var(--cyber-primary);
            opacity: 0.7;
        }

        /* Code Block Styling */
        code {
            font-family: 'Fira Code', monospace;
            background: rgba(0, 0, 0, 0.5);
            color: var(--cyber-gold);
            padding: 0.2rem 0.5rem;
            border-radius: 4px;
            font-size: 0.9rem;
            border: 1px solid rgba(255, 215, 0, 0.3);
        }

        /* Selection Styling */
        ::selection {
            background: rgba(0, 255, 136, 0.3);
            color: var(--text-primary);
        }

        ::-moz-selection {
            background: rgba(0, 255, 136, 0.3);
            color: var(--text-primary);
        }

        /* Scrollbar Styling for All Elements */
        ::-webkit-scrollbar {
            width: 10px;
        }

        ::-webkit-scrollbar-track {
            background: rgba(0, 0, 0, 0.3);
            border-radius: 5px;
        }

        ::-webkit-scrollbar-thumb {
            background: var(--gradient-cyber);
            border-radius: 5px;
        }

        ::-webkit-scrollbar-thumb:hover {
            background: var(--cyber-primary);
        }

        /* Enhanced Grid Animation */
        .cyber-grid::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: radial-gradient(circle at 50% 50%, rgba(0, 255, 136, 0.1) 0%, transparent 70%);
            animation: pulse 4s ease-in-out infinite;
        }

        /* Checker Integration Status */
        .checker-status {
            background: rgba(0, 255, 136, 0.1);
            border: 1px solid var(--cyber-primary);
            border-radius: 10px;
            padding: 1rem;
            margin: 1rem 0;
            text-align: center;
            font-family: 'Orbitron', monospace;
            font-weight: 600;
        }

        .checker-status.active {
            color: var(--cyber-primary);
            box-shadow: 0 0 15px rgba(0, 255, 136, 0.3);
        }

        .checker-status.inactive {
            background: rgba(255, 51, 51, 0.1);
            border-color: var(--cyber-red);
            color: var(--cyber-red);
        }
    </style>
</head>
<body>
    <div class="cyber-grid"></div>
    <canvas class="cyber-matrix" id="matrixCanvas"></canvas>
    
    <!-- Enhanced Header -->
    <header class="cyber-header">
        <div class="header-content">
            <a href="https://w3llstore.com/" class="cyber-logo glitch" target="_blank">
                <i class="fas fa-torii-gate"></i>
                <span>W3LL CYBER</span>
                <small class="japanese-text" style="font-size: 0.6em; color: var(--cyber-gold);">侍</small>
            </a>
            <nav class="nav-links">
                <a href="https://w3llstore.com/" class="nav-link" target="_blank">
                    <i class="fas fa-home"></i> HOME
                </a>
                <a href="https://t.me/W3LLSTORE_ADMIN" class="nav-link" target="_blank">
                    <i class="fab fa-telegram"></i> ADMIN
                </a>
                <a href="https://t.me/+vJV6tnAIbIU2ZWRi" class="nav-link" target="_blank">
                    <i class="fas fa-satellite-dish"></i> CHANNEL
                </a>
            </nav>
        </div>
    </header>

    <div class="container">
        <!-- Checker Integration Status -->
        <div class="checker-status active">
            <i class="fas fa-shield-check"></i>
            CHECKER INTEGRATION: ACTIVE | 
            <span class="japanese-text">チェッカー統合：有効</span> | 
            <small>Endpoints: /valid, /test, /delivery, /health</small>
        </div>

        <div class="row">
            <!-- Main Mailer Panel -->
            <div class="col-lg-8">
                <div class="cyber-card">
                    <div class="card-header">
                        <h1 class="card-title">
                            <i class="fas fa-dragon"></i>
                            ENHANCED MASS MAILER PROTOCOL
                            <small class="japanese-text" style="font-size: 0.5em; color: var(--cyber-gold);">大量メール送信システム</small>
                        </h1>
                    </div>
                    <div class="card-body">
                        <form method="POST" id="mailerForm">
                            <!-- SMTP Toggle -->
                            <div class="cyber-checkbox">
                                <input type="checkbox" name="useSmtp" value="1" <?= $_59?'checked':'' ?> id="useSmtp">
                                <label for="useSmtp">
                                    <i class="fas fa-server"></i>
                                    Enable SMTP Protocol (Recommended for Mass Sending)
                                    <small class="japanese-text" style="color: var(--text-secondary);">推奨設定</small>
                                </label>
                            </div>
                            
                            <!-- SMTP Configuration Panel -->
                            <div class="smtp-panel" id="smtpConfig" style="<?= $_59?'':'display:none;' ?>">
                                <div class="form-grid">
                                    <div class="form-group">
                                        <label class="form-label">
                                            <i class="fas fa-server"></i>
                                            SMTP HOST <span class="japanese-text">サーバー</span>
                                        </label>
                                        <input type="text" class="cyber-input" name="smtpHost" 
                                               value="<?= htmlspecialchars($_60)?>" 
                                               placeholder="smtp.gmail.com">
                                    </div>
                                    <div class="form-group">
                                        <label class="form-label">
                                            <i class="fas fa-plug"></i>
                                            PORT <span class="japanese-text">ポート</span>
                                        </label>
                                        <input type="number" class="cyber-input" name="smtpPort" 
                                               value="<?= $_61 ?>" placeholder="587">
                                    </div>
                                    <div class="form-group">
                                        <label class="form-label">
                                            <i class="fas fa-shield-alt"></i>
                                            ENCRYPTION <span class="japanese-text">暗号化</span>
                                        </label>
                                        <select class="cyber-select" name="smtpEncryption">
                                            <option value="tls" <?= $_64=='tls'?'selected':'' ?>>TLS</option>
                                            <option value="ssl" <?= $_64=='ssl'?'selected':'' ?>>SSL</option>
                                            <option value="none" <?= $_64=='none'?'selected':'' ?>>None</option>
                                        </select>
                                    </div>
                                    <div class="form-group">
                                        <label class="form-label">
                                            <i class="fas fa-envelope"></i>
                                            SMTP EMAIL <span class="japanese-text">メール</span>
                                        </label>
                                        <input type="email" class="cyber-input" name="smtpEmail" 
                                               value="<?= htmlspecialchars($_62)?>" 
                                               placeholder="noreply@example.com">
                                    </div>
                                    <div class="form-group">
                                        <label class="form-label">
                                            <i class="fas fa-key"></i>
                                            SMTP PASSWORD <span class="japanese-text">パスワード</span>
                                        </label>
                                        <input type="password" class="cyber-input" name="smtpPassword" 
                                               value="<?= htmlspecialchars($_63)?>" 
                                               placeholder="••••••••••••">
                                    </div>
                                </div>
                            </div>
                            
                            <!-- Email Configuration -->
                            <div class="form-grid">
                                <div class="form-group">
                                    <label class="form-label">
                                        <i class="fas fa-paper-plane"></i>
                                        SENDER EMAIL <span class="japanese-text">送信者</span>
                                    </label>
                                    <input type="email" class="cyber-input" name="senderEmail" 
                                           value="<?= htmlspecialchars($_53)?>" 
                                           placeholder="sender@example.com" required>
                                </div>
                                <div class="form-group">
                                    <label class="form-label">
                                        <i class="fas fa-user-ninja"></i>
                                        SENDER NAME <span class="japanese-text">送信者名</span>
                                    </label>
                                    <input type="text" class="cyber-input" name="senderName" 
                                           value="<?= htmlspecialchars($_54)?>" 
                                           placeholder="Cyber Samurai 侍" required>
                                </div>
                                <div class="form-group">
                                    <label class="form-label">
                                        <i class="fas fa-reply"></i>
                                        REPLY-TO EMAIL <span class="japanese-text">返信先</span>
                                    </label>
                                    <input type="email" class="cyber-input" name="replyTo" 
                                           value="<?= htmlspecialchars($_26)?>" 
                                           placeholder="reply@example.com">
                                </div>
                                <div class="form-group">
                                    <label class="form-label">
                                        <i class="fas fa-code"></i>
                                        MESSAGE TYPE <span class="japanese-text">形式</span>
                                    </label>
                                    <div class="radio-group">
                                        <div class="cyber-radio">
                                            <input type="radio" name="messageType" value="1" 
                                                   <?= $_33 ?> id="html">
                                                   <label for="html">HTML</label>
                                        </div>
                                        <div class="cyber-radio">
                                            <input type="radio" name="messageType" value="2" 
                                                   <?= $_65 ?> id="plain">
                                            <label for="plain">Plain Text</label>
                                        </div>
                                    </div>
                                </div>
                            </div>
                            
                            <!-- Subject -->
                            <div class="form-group">
                                <label class="form-label">
                                    <i class="fas fa-tag"></i>
                                    EMAIL SUBJECT <span class="japanese-text">件名</span>
                                </label>
                                <input type="text" class="cyber-input" name="subject" 
                                       value="<?= htmlspecialchars($_55)?>" 
                                       placeholder="W3LL Cyber Security Alert - [-time-] 🔐" required>
                            </div>
                            
                            <!-- Message and Email List -->
                            <div class="form-grid">
                                <div class="form-group">
                                    <label class="form-label">
                                        <i class="fas fa-scroll"></i>
                                        MESSAGE CONTENT <span class="japanese-text">メッセージ</span>
                                    </label>
                                    <textarea class="cyber-textarea" name="messageLetter" required 
                                              placeholder="Enter your message content here... メッセージをここに入力してください&#10;&#10;Available variables 利用可能な変数:&#10;[-email-] = Recipient email 受信者メール&#10;[-emailuser-] = Email username ユーザー名&#10;[-time-] = Current time 現在時刻&#10;[-randomstring-] = Random string ランダム文字列&#10;[-randomnumber-] = Random number ランダム数字"><?= htmlspecialchars($_58)?></textarea>
                                </div>
                                <div class="form-group">
                                    <label class="form-label">
                                        <i class="fas fa-list"></i>
                                        TARGET EMAIL LIST <span class="japanese-text">対象リスト</span>
                                    </label>
                                    <textarea class="cyber-textarea" name="emailList" required 
                                              placeholder="Enter email addresses (one per line) 1行に1つのメールアドレス:&#10;&#10;user1@example.com&#10;user2@example.com&#10;user3@example.com"><?= htmlspecialchars($_56)?></textarea>
                                </div>
                            </div>
                            
                            <!-- Action Buttons -->
                            <div class="button-group">
                                <button type="submit" name="action" value="send" class="cyber-btn btn-primary">
                                    <i class="fas fa-rocket"></i>
                                    EXECUTE MASS MISSION <span class="japanese-text">実行</span>
                                </button>
                                <button type="button" class="cyber-btn btn-secondary" onclick="testSmtpConnection()">
                                    <i class="fas fa-vial"></i>
                                    TEST PROTOCOL <span class="japanese-text">テスト</span>
                                </button>
                                <button type="button" class="cyber-btn btn-danger" onclick="resetForm()">
                                    <i class="fas fa-power-off"></i>
                                    RESET SYSTEM <span class="japanese-text">リセット</span>
                                </button>
                            </div>
                        </form>
                    </div>
                </div>
            </div>
            
            <!-- Instructions Panel -->
            <div class="col-lg-4">
                <div class="cyber-card">
                    <div class="card-header">
                        <h2 class="card-title">
                            <i class="fas fa-terminal"></i>
                            CONTROL MANUAL
                            <small class="japanese-text" style="font-size: 0.5em; color: var(--cyber-gold);">操作説明書</small>
                        </h2>
                    </div>
                    <div class="card-body">
                        <!-- Checker Integration Info -->
                        <div class="instructions-panel" style="background: rgba(0, 255, 136, 0.05); border-color: var(--cyber-primary);">
                            <h3 class="instructions-title">
                                <i class="fas fa-shield-check"></i>
                                CHECKER INTEGRATION <span class="japanese-text">チェッカー統合</span>
                            </h3>
                            <ul style="list-style: none; padding: 0; color: var(--text-secondary); line-height: 1.8;">
                                <li><i class="fas fa-check" style="color: var(--cyber-primary); margin-right: 0.5rem;"></i><code>?valid</code> - Validation endpoint <span class="japanese-text">検証エンドポイント</span></li>
                                <li><i class="fas fa-check" style="color: var(--cyber-primary); margin-right: 0.5rem;"></i><code>?test&email=xxx</code> - Test email sending <span class="japanese-text">メール送信テスト</span></li>
                                <li><i class="fas fa-check" style="color: var(--cyber-primary); margin-right: 0.5rem;"></i><code>?delivery&email=xxx</code> - Delivery test <span class="japanese-text">配信テスト</span></li>
                                <li><i class="fas fa-check" style="color: var(--cyber-primary); margin-right: 0.5rem;"></i><code>?health</code> - Health check <span class="japanese-text">ヘルスチェック</span></li>
                                <li><i class="fas fa-check" style="color: var(--cyber-primary); margin-right: 0.5rem;"></i><code>?check_capability</code> - Capability check <span class="japanese-text">機能チェック</span></li>
                            </ul>
                        </div>

                        <div class="instructions-panel">
                            <h3 class="instructions-title">
                                <i class="fas fa-code"></i>
                                DYNAMIC VARIABLES <span class="japanese-text">動的変数</span>
                            </h3>
                            <ul class="variable-list">
                                <li>
                                    <code class="variable-code">[-email-]</code>
                                    <span>Recipient Email <span class="japanese-text">受信者メール</span></span>
                                </li>
                                <li>
                                    <code class="variable-code">[-emailuser-]</code>
                                    <span>Email Username <span class="japanese-text">ユーザー名</span></span>
                                </li>
                                <li>
                                    <code class="variable-code">[-time-]</code>
                                    <span>Current Timestamp <span class="japanese-text">現在時刻</span></span>
                                </li>
                                <li>
                                    <code class="variable-code">[-randomstring-]</code>
                                    <span>Random Alphanumeric <span class="japanese-text">ランダム英数</span></span>
                                </li>
                                <li>
                                    <code class="variable-code">[-randomnumber-]</code>
                                    <span>Random Numeric <span class="japanese-text">ランダム数字</span></span>
                                </li>
                                <li>
                                    <code class="variable-code">[-randomletters-]</code>
                                    <span>Random Letters <span class="japanese-text">ランダム文字</span></span>
                                </li>
                                <li>
                                    <code class="variable-code">[-randommd5-]</code>
                                    <span>Random MD5 Hash <span class="japanese-text">MD5ハッシュ</span></span>
                                </li>
                            </ul>
                        </div>
                        
                        <div class="instructions-panel">
                            <h3 class="instructions-title">
                                <i class="fas fa-info-circle"></i>
                                SYSTEM STATUS <span class="japanese-text">システム状態</span>
                            </h3>
                            <div style="display: flex; flex-direction: column; gap: 0.8rem;">
                                <div style="display: flex; justify-content: space-between; align-items: center;">
                                    <strong>Server IP <span class="japanese-text">サーバーIP</span>:</strong>
                                    <code><?= $_SERVER['SERVER_ADDR']?? gethostbyname(gethostname())?></code>
                                </div>
                                <div style="display: flex; justify-content: space-between; align-items: center;">
                                    <strong>PHP Version <span class="japanese-text">PHPバージョン</span>:</strong>
                                    <code><?= phpversion()?></code>
                                </div>
                                <div style="display: flex; justify-content: space-between; align-items: center;">
                                    <strong>Mail Function <span class="japanese-text">メール機能</span>:</strong>
                                    <span class="<?= function_exists('mail')?'status-success':'status-danger' ?>">
                                        <?= function_exists('mail')?'✓ ACTIVE':'✗ DISABLED' ?>
                                    </span>
                                </div>
                                <div style="display: flex; justify-content: space-between; align-items: center;">
                                    <strong>SMTP Support <span class="japanese-text">SMTP対応</span>:</strong>
                                    <span class="<?= function_exists('fsockopen')?'status-success':'status-danger' ?>">
                                        <?= function_exists('fsockopen')?'✓ ENABLED':'✗ DISABLED' ?>
                                    </span>
                                </div>
                                <div style="display: flex; justify-content: space-between; align-items: center;">
                                    <strong>OpenSSL <span class="japanese-text">暗号化</span>:</strong>
                                    <span class="<?= extension_loaded('openssl')?'status-success':'status-danger' ?>">
                                        <?= extension_loaded('openssl')?'✓ LOADED':'✗ MISSING' ?>
                                    </span>
                                </div>
                                <div style="display: flex; justify-content: space-between; align-items: center;">
                                    <strong>Memory Limit <span class="japanese-text">メモリ制限</span>:</strong>
                                    <code><?= ini_get('memory_limit')?></code>
                                </div>
                                <div style="display: flex; justify-content: space-between; align-items: center;">
                                    <strong>Max Execution <span class="japanese-text">実行時間</span>:</strong>
                                    <code><?= ini_get('max_execution_time')?>s</code>
                                </div>
                                <div style="display: flex; justify-content: space-between; align-items: center;">
                                    <strong>Checker Status <span class="japanese-text">チェッカー状態</span>:</strong>
                                    <span class="status-success">✓ INTEGRATED</span>
                                </div>
                            </div>
                        </div>
                        
                        <div class="instructions-panel">
                            <h3 class="instructions-title">
                                <i class="fas fa-shield-alt"></i>
                                SECURITY PROTOCOLS <span class="japanese-text">セキュリティ</span>
                            </h3>
                            <ul style="list-style: none; padding: 0; color: var(--text-secondary); line-height: 1.8;">
                                <li><i class="fas fa-check" style="color: var(--cyber-primary); margin-right: 0.5rem;"></i>Email validation enabled <span class="japanese-text">メール検証有効</span></li>
                                <li><i class="fas fa-check" style="color: var(--cyber-primary); margin-right: 0.5rem;"></i>DNS MX record verification <span class="japanese-text">DNS検証</span></li>
                                <li><i class="fas fa-check" style="color: var(--cyber-primary); margin-right: 0.5rem;"></i>Anti-spam headers included <span class="japanese-text">スパム対策</span></li>
                                <li><i class="fas fa-check" style="color: var(--cyber-primary); margin-right: 0.5rem;"></i>Rate limiting protection <span class="japanese-text">レート制限</span></li>
                                <li><i class="fas fa-check" style="color: var(--cyber-primary); margin-right: 0.5rem;"></i>TLS/SSL encryption support <span class="japanese-text">暗号化対応</span></li>
                                <li><i class="fas fa-check" style="color: var(--cyber-primary); margin-right: 0.5rem;"></i>Checker integration active <span class="japanese-text">チェッカー統合有効</span></li>
                            </ul>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        
        <?php if($_POST['action']=="send"):?>
        <!-- Results Panel -->
        <div class="cyber-card results-panel">
            <div class="results-header">
                <i class="fas fa-satellite-dish"></i>
                MISSION EXECUTION RESULTS
                <span class="japanese-text" style="font-size: 0.7em;">実行結果</span>
                <div class="loading-spinner" id="loadingSpinner" style="margin-left: auto;"></div>
            </div>
            <div class="results-body">
                <div class="progress-bar">
                    <div class="progress-fill" id="progressBar"></div>
                </div>
                <div class="mass-results" id="resultsContainer">
                    <?php if(!empty($_56)){$_72=array_filter(array_map('trim',explode("\n",$_56)));$_73=count($_72);$_74=0;$_75=0;$_76=0;echo "<div style='text-align: center; margin-bottom: 2rem; font-family: \"Orbitron\", monospace;'>";echo "<h3 style='color: var(--cyber-primary);'>INITIATING MASS TRANSMISSION PROTOCOL</h3>";echo"<p style='color: var(--text-secondary);'>Processing <strong style='color: var(--cyber-gold);'>$_73</strong> target addresses <span class='japanese-text'>対象アドレス処理中</span></p>";echo "</div>";$_70=new W3LLMailer();if($_59&&!empty($_60)){$_70->isSMTP();$_70->$_37=$_60;$_70->$_40=$_61;$_70->$_45=!empty($_62)&&!empty($_63);$_70->$_46=$_62;$_70->$_47=$_63;$_70->$_38=$_64;}else{$_70->isMail();}$_70->setFrom($_53,$_54);if(!empty($_26)){$_70->addReplyTo($_26);}$_70->isHTML($_57==1);foreach($_72 as $_77=>$_4){$_78=$_77+1;$_4=trim($_4);echo "<div class='email-row'>";echo"<div class='email-counter'>#$_78</div>";echo"<div class='email-address'>$_4</div>";echo "<div class='email-status'>";if(!w3llMailCheck($_4)){echo "<span class='status-badge status-invalid'>INVALID</span>";$_76++;}else{$_70->clearAddresses();$_70->addAddress($_4);$_79=w3llClear($_55,$_4);$_80=w3llClear($_58,$_4);$_70->$_50=$_79;$_70->$_51=$_80;if($_70->send()){echo "<span class='status-badge status-ok'>SENT</span>";$_74++;}else{echo "<span class='status-badge status-fail'>FAILED</span>";$_75++;if(!empty($_70->$_43)){error_log("W3LL Mailer Error for $_4: ".$_70->$_43);}}}echo "</div>";echo "</div>";usleep(100000);if(ob_get_level()){ob_flush();}flush();}echo "<div style='margin-top: 3rem; padding: 2rem; background: rgba(0, 0, 0, 0.3); border-radius: 15px; text-align: center; font-family: \"Orbitron\", monospace;'>";echo "<h3 style='color: var(--cyber-primary); margin-bottom: 1.5rem;'>MISSION COMPLETION REPORT <span class='japanese-text' style='font-size: 0.6em; color: var(--cyber-gold);'>任務完了報告</span></h3>";echo "<div style='display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 1.5rem; margin-bottom: 2rem;'>";echo "<div style='background: rgba(0, 255, 136, 0.1); padding: 1.5rem; border-radius: 12px; border: 1px solid var(--cyber-primary);'>";echo"<div style='font-size: 2rem; font-weight: 900; color: var(--cyber-primary);'>$_74</div>";echo "<div style='color: var(--text-secondary);'>SUCCESSFUL <span class='japanese-text'>成功</span></div>";echo "</div>";echo "<div style='background: rgba(255, 51, 51, 0.1); padding: 1.5rem; border-radius: 12px; border: 1px solid var(--cyber-red);'>";echo"<div style='font-size: 2rem; font-weight: 900; color: var(--cyber-red);'>$_75</div>";echo "<div style='color: var(--text-secondary);'>FAILED <span class='japanese-text'>失敗</span></div>";echo "</div>";echo "<div style='background: rgba(255, 136, 0, 0.1); padding: 1.5rem; border-radius: 12px; border: 1px solid var(--cyber-orange);'>";echo"<div style='font-size: 2rem; font-weight: 900; color: var(--cyber-orange);'>$_76</div>";echo "<div style='color: var(--text-secondary);'>INVALID <span class='japanese-text'>無効</span></div>";echo "</div>";echo "<div style='background: rgba(0, 128, 255, 0.1); padding: 1.5rem; border-radius: 12px; border: 1px solid var(--cyber-tertiary);'>";echo"<div style='font-size: 2rem; font-weight: 900; color: var(--cyber-tertiary);'>$_73</div>";echo "<div style='color: var(--text-secondary);'>TOTAL <span class='japanese-text'>合計</span></div>";echo "</div>";echo "</div>";$_81=$_73>0?round(($_74/$_73)*100,2):0;$_82=$_81>=80?'var(--cyber-primary)':($_81>=50?'var(--cyber-orange)':'var(--cyber-red)');echo"<div style='background: rgba(0, 0, 0, 0.5); padding: 1.5rem; border-radius: 12px; border: 2px solid $_82;'>";echo"<div style='font-size: 1.5rem; font-weight: 700; color: $_82; margin-bottom: 0.5rem;'>SUCCESS RATE: $_81%</div>";echo "<div style='color: var(--text-secondary);'>Mission efficiency rating <span class='japanese-text'>任務効率評価</span></div>";echo "</div>";echo "<div style='margin-top: 2rem; padding: 1rem; background: rgba(0, 255, 136, 0.05); border: 1px solid rgba(0, 255, 136, 0.2); border-radius: 10px;'>";echo "<p style='color: var(--text-secondary); margin: 0; font-size: 0.9rem;'>";echo "<i class='fas fa-info-circle' style='color: var(--cyber-primary); margin-right: 0.5rem;'></i>";echo "Transmission completed at <strong style='color: var(--cyber-gold);'>".date('Y-m-d H:i:s')."</strong> ";echo "<span class='japanese-text'>送信完了時刻</span>";echo "</p>";echo "</div>";echo "</div>";}?>
                </div>
            </div>
        </div>
        
        <script>
        // Animate progress bar
        document.addEventListener('DOMContentLoaded', function() {
            const progressBar = document.getElementById('progressBar');
            const spinner = document.getElementById('loadingSpinner');
            
            let progress = 0;
            const interval = setInterval(() => {
                progress += 2;
                progressBar.style.width = progress + '%';
                
                if (progress >= 100) {
                    clearInterval(interval);
                    spinner.style.display = 'none';
                    
                    // Show completion notification
                    showNotification('Mission completed successfully! 任務完了！', 'success');
                }
            }, 100);
        });
        </script>
        <?php endif;?>
    </div>
    
    <!-- Enhanced Footer -->
    <footer class="cyber-footer">
        <div class="footer-content">
            <div class="footer-links">
                <a href="https://w3llstore.com/" class="footer-link" target="_blank">
                    <i class="fas fa-globe"></i>
                    W3LL STORE
                </a>
                <a href="https://t.me/W3LLSTORE_ADMIN" class="footer-link" target="_blank">
                    <i class="fab fa-telegram"></i>
                    ADMIN CONTACT
                </a>
                <a href="https://t.me/+vJV6tnAIbIU2ZWRi" class="footer-link" target="_blank">
                    <i class="fas fa-broadcast-tower"></i>
                    UPDATES CHANNEL
                </a>
                <a href="mailto:support@w3llstore.com" class="footer-link">
                    <i class="fas fa-envelope"></i>
                    SUPPORT
                </a>
            </div>
            <div class="copyright">
                <p>W3LL CYBER SAMURAI MAILER v3.2 Enhanced Edition with Checker Integration <span class="japanese-text">サイバー侍メーラー</span></p>
                <p>&copy; 2024 W3LL Store. Advanced Mass Email System with LeafMailer Integration + Checker Support.</p>
                <p style="font-size: 0.8rem; margin-top: 1rem; color: var(--text-tertiary);">
                    Built with cutting-edge technology for professional email marketing campaigns.<br>
                    <span class="japanese-text">プロフェッショナルなメールマーケティングキャンペーンのための最先端技術で構築</span><br>
                    <strong style="color: var(--cyber-primary);">✓ Checker Integration Active | チェッカー統合有効</strong>
                </p>
            </div>
        </div>
    </footer>
    
    <!-- Matrix Rain Effect Script -->
    <script>
        // Matrix Rain Effect
        const canvas = document.getElementById('matrixCanvas');
        const ctx = canvas.getContext('2d');
        
        canvas.width = window.innerWidth;
        canvas.height = window.innerHeight;
        
        const katakana = 'アァカサタナハマヤャラワガザダバパイィキシチニヒミリヰギジヂビピウゥクスツヌフムユュルグズブヅプエェケセテネヘメレヱゲゼデベペオォコソトノホモヨョロヲゴゾドボポヴッン';
        const latin = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ';
        const nums = '0123456789';
        const alphabet = katakana + latin + nums;
        
        const fontSize = 16;
        const columns = canvas.width / fontSize;
        
        const rainDrops = [];
        
        for (let x = 0; x < columns; x++) {
            rainDrops[x] = 1;
        }
        
        const draw = () => {
            ctx.fillStyle = 'rgba(0, 0, 0, 0.05)';
            ctx.fillRect(0, 0, canvas.width, canvas.height);
            
            ctx.fillStyle = '#00ff88';
            ctx.font = fontSize + 'px monospace';
            
            for (let i = 0; i < rainDrops.length; i++) {
                const text = alphabet.charAt(Math.floor(Math.random() * alphabet.length));
                ctx.fillText(text, i * fontSize, rainDrops[i] * fontSize);
                
                if (rainDrops[i] * fontSize > canvas.height && Math.random() > 0.975) {
                    rainDrops[i] = 0;
                }
                rainDrops[i]++;
            }
        };
        
        setInterval(draw, 30);
        
        // Resize handler
        window.addEventListener('resize', () => {
            canvas.width = window.innerWidth;
            canvas.height = window.innerHeight;
        });
        
        // Enhanced JavaScript Functions
        function toggleSmtpConfig() {
            const checkbox = document.getElementById('useSmtp');
            const config = document.getElementById('smtpConfig');
            config.style.display = checkbox.checked ? 'block' : 'none';
        }
        
        document.getElementById('useSmtp').addEventListener('change', toggleSmtpConfig);
        
        function testSmtpConnection() {
            const useSmtp = document.getElementById('useSmtp').checked;
            
            if (!useSmtp) {
                showNotification('Please enable SMTP first! SMTPを有効にしてください！', 'warning');
                return;
            }
            
            const host = document.querySelector('input[name="smtpHost"]').value;
            const port = document.querySelector('input[name="smtpPort"]').value;
            const email = document.querySelector('input[name="smtpEmail"]').value;
            const password = document.querySelector('input[name="smtpPassword"]').value;
            
            if (!host || !email || !password) {
                showNotification('Please fill all SMTP fields! 全てのSMTP項目を入力してください！', 'error');
                return;
            }
            
            showNotification('Testing SMTP connection... SMTP接続をテスト中...', 'info');
            
            // Test checker integration
            fetch(window.location.href + '?test&email=' + encodeURIComponent(email))
                .then(response => response.json())
                .then(data => {
                    if (data.status === 'ok' && data.email_sent) {
                        showNotification('SMTP connection successful! Test email sent! SMTP接続成功！テストメール送信完了！', 'success');
                    } else {
                        showNotification('SMTP connection failed: ' + (data.error || 'Unknown error') + ' SMTP接続失敗！', 'error');
                    }
                })
                .catch(error => {
                    showNotification('Connection test failed: ' + error.message + ' 接続テスト失敗！', 'error');
                });
        }
        
        function resetForm() {
            if (confirm('Are you sure you want to reset all fields? 全てのフィールドをリセットしますか？')) {
                document.getElementById('mailerForm').reset();
                document.getElementById('smtpConfig').style.display = 'none';
                showNotification('Form reset successfully! フォームがリセットされました！', 'info');
            }
        }
        
        function showNotification(message, type = 'info') {
                        // Remove existing notifications
                        const existing = document.querySelectorAll('.notification');
            existing.forEach(n => n.remove());
            
            const notification = document.createElement('div');
            notification.className = 'notification';
            
            let icon, color;
            switch(type) {
                case 'success':
                    icon = 'fas fa-check-circle';
                    color = 'var(--cyber-primary)';
                    break;
                case 'error':
                    icon = 'fas fa-exclamation-triangle';
                    color = 'var(--cyber-red)';
                    break;
                case 'warning':
                    icon = 'fas fa-exclamation-circle';
                    color = 'var(--cyber-orange)';
                    break;
                default:
                    icon = 'fas fa-info-circle';
                    color = 'var(--cyber-tertiary)';
            }
            
            notification.innerHTML = `
                <i class="${icon}" style="color: ${color}; font-size: 1.2rem;"></i>
                <span>${message}</span>
            `;
            
            notification.style.borderColor = color;
            
            document.body.appendChild(notification);
            
            // Auto remove after 5 seconds
            setTimeout(() => {
                notification.style.opacity = '0';
                notification.style.transform = 'translateX(100%)';
                setTimeout(() => notification.remove(), 300);
            }, 5000);
        }
        
        // Form validation
        document.getElementById('mailerForm').addEventListener('submit', function(e) {
            const senderEmail = document.querySelector('input[name="senderEmail"]').value;
            const subject = document.querySelector('input[name="subject"]').value;
            const message = document.querySelector('textarea[name="messageLetter"]').value;
            const emailList = document.querySelector('textarea[name="emailList"]').value;
            
            if (!senderEmail || !subject || !message || !emailList) {
                e.preventDefault();
                showNotification('Please fill all required fields! 必須項目を全て入力してください！', 'error');
                return;
            }
            
            const emailCount = emailList.trim().split('\n').filter(email => email.trim()).length;
            if (emailCount === 0) {
                e.preventDefault();
                showNotification('Please enter at least one email address! 最低1つのメールアドレスを入力してください！', 'error');
                return;
            }
            
            if (emailCount > 1000) {
                if (!confirm(`You are about to send ${emailCount} emails. This may take a while. Continue? ${emailCount}通のメールを送信します。時間がかかる場合があります。続行しますか？`)) {
                    e.preventDefault();
                    return;
                }
            }
            
            showNotification(`Initiating mass email transmission to ${emailCount} targets... ${emailCount}件の対象にメール送信を開始します...`, 'info');
        });
        
        // Auto-save form data to localStorage
        const formInputs = document.querySelectorAll('input, textarea, select');
        formInputs.forEach(input => {
            // Load saved data
            const savedValue = localStorage.getItem('w3ll_mailer_' + input.name);
            if (savedValue && input.type !== 'password') {
                if (input.type === 'checkbox') {
                    input.checked = savedValue === 'true';
                } else {
                    input.value = savedValue;
                }
            }
            
            // Save data on change
            input.addEventListener('change', function() {
                if (input.type === 'password') return; // Don't save passwords
                
                const value = input.type === 'checkbox' ? input.checked : input.value;
                localStorage.setItem('w3ll_mailer_' + input.name, value);
            });
        });
        
        // Initialize SMTP config visibility
        toggleSmtpConfig();
        
        // Add typing effect to placeholders
        function typeWriter(element, text, speed = 50) {
            let i = 0;
            element.placeholder = '';
            
            function type() {
                if (i < text.length) {
                    element.placeholder += text.charAt(i);
                    i++;
                    setTimeout(type, speed);
                }
            }
            type();
        }
        
        // Apply typing effect to some inputs
        document.addEventListener('DOMContentLoaded', function() {
            const emailInput = document.querySelector('input[name="senderEmail"]');
            if (emailInput && !emailInput.value) {
                setTimeout(() => {
                    typeWriter(emailInput, 'cyber.samurai@w3llstore.com', 100);
                }, 1000);
            }
            
            // Test checker integration on page load
            testCheckerIntegration();
        });
        
        // Checker Integration Test Function
        function testCheckerIntegration() {
            fetch(window.location.href + '?valid')
                .then(response => response.json())
                .then(data => {
                    if (data.w3ll_signature === 'W3LL_CYBER_SAMURAI_VERIFIED') {
                        console.log('%c🥷 Checker Integration: ACTIVE | チェッカー統合：有効', 'color: #00ff88; font-weight: bold;');
                        console.log('%cEndpoints available:', 'color: #ffd700;');
                        console.log('%c- ?valid - Validation endpoint', 'color: #0080ff;');
                        console.log('%c- ?test&email=xxx - Test email sending', 'color: #0080ff;');
                        console.log('%c- ?delivery&email=xxx - Delivery test', 'color: #0080ff;');
                        console.log('%c- ?health - Health check', 'color: #0080ff;');
                        console.log('%c- ?check_capability - Capability check', 'color: #0080ff;');
                        
                        // Update checker status indicator
                        const checkerStatus = document.querySelector('.checker-status');
                        if (checkerStatus) {
                            checkerStatus.innerHTML = `
                                <i class="fas fa-shield-check"></i>
                                CHECKER INTEGRATION: VERIFIED | 
                                <span class="japanese-text">チェッカー統合：検証済み</span> | 
                                <small>Version: ${data.version || '3.2 Enhanced'}</small>
                            `;
                        }
                    }
                })
                .catch(error => {
                    console.log('%c⚠️ Checker Integration Test Failed', 'color: #ff3333; font-weight: bold;');
                });
        }
        
        // Cyber glitch effect on hover
        document.querySelectorAll('.glitch').forEach(element => {
            element.addEventListener('mouseenter', function() {
                this.style.animation = 'glitch 0.3s infinite';
            });
            
            element.addEventListener('mouseleave', function() {
                this.style.animation = 'glitch 2s infinite';
            });
        });
        
        // Enhanced SMTP Test with Checker Integration
        function advancedSmtpTest() {
            const testEmail = prompt('Enter test email address for SMTP verification:\nテスト用メールアドレスを入力してください:');
            
            if (!testEmail || !testEmail.includes('@')) {
                showNotification('Invalid email address! 無効なメールアドレス！', 'error');
                return;
            }
            
            showNotification('Running advanced SMTP test with checker integration... 高度なSMTPテストを実行中...', 'info');
            
            // Test multiple endpoints
            Promise.all([
                fetch(window.location.href + '?test&email=' + encodeURIComponent(testEmail)),
                fetch(window.location.href + '?delivery&email=' + encodeURIComponent(testEmail)),
                fetch(window.location.href + '?health')
            ])
            .then(responses => Promise.all(responses.map(r => r.json())))
            .then(results => {
                const [testResult, deliveryResult, healthResult] = results;
                
                let message = 'Advanced SMTP Test Results:\n高度なSMTPテスト結果:\n\n';
                message += `✓ Test Email: ${testResult.email_sent ? 'SENT' : 'FAILED'}\n`;
                message += `✓ Delivery Test: ${deliveryResult.delivered ? 'OK' : 'FAILED'}\n`;
                message += `✓ Health Check: ${healthResult.status === 'healthy' ? 'HEALTHY' : 'UNHEALTHY'}\n`;
                
                if (testResult.email_sent && deliveryResult.delivered && healthResult.status === 'healthy') {
                    showNotification('All tests passed! SMTP is working perfectly! 全テスト合格！SMTP完全動作！', 'success');
                } else {
                    showNotification('Some tests failed. Check configuration. 一部テスト失敗。設定を確認してください。', 'warning');
                }
                
                console.log(message);
            })
            .catch(error => {
                showNotification('Advanced test failed: ' + error.message, 'error');
            });
        }
        
        // Add advanced test button functionality
        document.addEventListener('DOMContentLoaded', function() {
            // Add advanced test button
            const buttonGroup = document.querySelector('.button-group');
            if (buttonGroup) {
                const advancedTestBtn = document.createElement('button');
                advancedTestBtn.type = 'button';
                advancedTestBtn.className = 'cyber-btn btn-secondary';
                advancedTestBtn.innerHTML = '<i class="fas fa-microscope"></i> ADVANCED TEST <span class="japanese-text">高度テスト</span>';
                advancedTestBtn.onclick = advancedSmtpTest;
                buttonGroup.appendChild(advancedTestBtn);
            }
        });
        
        // Console easter egg with checker info
        console.log(`
    ██╗    ██╗██████╗ ██╗     ██╗         ███████╗████████╗ ██████╗ ██████╗ ███████╗
    ██║    ██║╚════██╗██║     ██║         ██╔════╝╚══██╔══╝██╔═══██╗██╔══██╗██╔════╝
    ██║ █╗ ██║ █████╔╝██║     ██║         ███████╗   ██║   ██║   ██║██████╔╝█████╗  
    ██║███╗██║ ╚═══██╗██║     ██║         ╚════██║   ██║   ██║   ██║██╔══██╗██╔══╝  
    ╚███╔███╔╝██████╔╝███████╗███████╗    ███████║   ██║   ╚██████╔╝██║  ██║███████╗
     ╚══╝╚══╝ ╚═════╝ ╚══════╝╚══════╝    ╚══════╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝╚══════╝
                                                                                      
    🥷 CYBER SAMURAI MAILER v3.2 Enhanced Edition + Checker Integration
    🌸 Built with honor and precision | 名誉と精密さで構築
    🔥 Advanced Mass Email System by W3LL Store
    ⚡ https://w3llstore.com/ | Telegram: @W3LLSTORE_ADMIN
    🛡️ Checker Integration: ACTIVE | チェッカー統合：有効
        `);
        
        console.log('%c🥷 Welcome to the Cyber Dojo! サイバー道場へようこそ！', 'color: #00ff88; font-size: 16px; font-weight: bold;');
        console.log('%c🛡️ Checker Integration Endpoints:', 'color: #ffd700; font-size: 14px; font-weight: bold;');
        console.log('%c• ?valid - Main validation endpoint', 'color: #0080ff; font-size: 12px;');
        console.log('%c• ?test&email=xxx&id=xxx - Test email sending', 'color: #0080ff; font-size: 12px;');
        console.log('%c• ?delivery&email=xxx&id=xxx - Delivery test', 'color: #0080ff; font-size: 12px;');
        console.log('%c• ?health - System health check', 'color: #0080ff; font-size: 12px;');
        console.log('%c• ?check_capability - Feature capability check', 'color: #0080ff; font-size: 12px;');
        console.log('%cFor support and premium tools, visit: https://w3llstore.com/', 'color: #ffd700; font-size: 14px;');
        
        // Real-time email validation
        const emailInputs = document.querySelectorAll('input[type="email"]');
        emailInputs.forEach(input => {
            input.addEventListener('blur', function() {
                const email = this.value.trim();
                if (email) {
                    validateEmailRealtime(email, this);
                }
            });
        });
        
        function validateEmailRealtime(email, inputElement) {
            // Visual feedback during validation
            inputElement.style.borderColor = 'var(--cyber-orange)';
            
            // Simple client-side validation first
            const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
            if (!emailRegex.test(email)) {
                inputElement.style.borderColor = 'var(--cyber-red)';
                return;
            }
            
            // Server-side validation via checker
            fetch(window.location.href + '?validate_email&email=' + encodeURIComponent(email))
                .then(response => response.json())
                .then(data => {
                    if (data.valid) {
                        inputElement.style.borderColor = 'var(--cyber-primary)';
                    } else {
                        inputElement.style.borderColor = 'var(--cyber-red)';
                    }
                })
                .catch(() => {
                    inputElement.style.borderColor = 'var(--cyber-primary)'; // Default to valid if check fails
                });
        }
        
        // Keyboard shortcuts
        document.addEventListener('keydown', function(e) {
            // Ctrl+Enter to send
            if (e.ctrlKey && e.key === 'Enter') {
                const sendBtn = document.querySelector('button[name="action"][value="send"]');
                if (sendBtn) {
                    sendBtn.click();
                }
            }
            
            // Ctrl+T to test SMTP
            if (e.ctrlKey && e.key === 't') {
                e.preventDefault();
                testSmtpConnection();
            }
            
            // Ctrl+R to reset form
            if (e.ctrlKey && e.key === 'r') {
                e.preventDefault();
                resetForm();
            }
        });
        
        // Add keyboard shortcuts info
        document.addEventListener('DOMContentLoaded', function() {
            const shortcutsInfo = document.createElement('div');
            shortcutsInfo.style.cssText = `
                position: fixed;
                bottom: 20px;
                left: 20px;
                background: rgba(26, 26, 46, 0.9);
                border: 1px solid var(--cyber-primary);
                border-radius: 10px;
                padding: 1rem;
                font-family: 'Fira Code', monospace;
                font-size: 0.8rem;
                color: var(--text-secondary);
                z-index: 1000;
                backdrop-filter: blur(10px);
            `;
            shortcutsInfo.innerHTML = `
                <div style="color: var(--cyber-primary); font-weight: bold; margin-bottom: 0.5rem;">
                    <i class="fas fa-keyboard"></i> Keyboard Shortcuts
                </div>
                <div>Ctrl+Enter: Send emails</div>
                <div>Ctrl+T: Test SMTP</div>
                <div>Ctrl+R: Reset form</div>
            `;
            document.body.appendChild(shortcutsInfo);
            
            // Hide shortcuts after 10 seconds
            setTimeout(() => {
                shortcutsInfo.style.opacity = '0';
                shortcutsInfo.style.transform = 'translateX(-100%)';
                setTimeout(() => shortcutsInfo.remove(), 500);
            }, 10000);
        });
        
        // Performance monitoring
        let performanceMetrics = {
            startTime: Date.now(),
            emailsSent: 0,
            errors: 0
        };
        
        function updatePerformanceMetrics(success) {
            if (success) {
                performanceMetrics.emailsSent++;
            } else {
                performanceMetrics.errors++;
            }
            
            const runtime = Date.now() - performanceMetrics.startTime;
            const rate = performanceMetrics.emailsSent / (runtime / 1000 / 60); // emails per minute
            
            console.log(`📊 Performance: ${performanceMetrics.emailsSent} sent, ${performanceMetrics.errors} errors, ${rate.toFixed(2)} emails/min`);
        }
        
        // Auto-backup form data
        function backupFormData() {
            const formData = new FormData(document.getElementById('mailerForm'));
            const backup = {};
            
            for (let [key, value] of formData.entries()) {
                if (key !== 'smtpPassword') { // Don't backup password
                    backup[key] = value;
                }
            }
            
            localStorage.setItem('w3ll_mailer_backup_' + Date.now(), JSON.stringify(backup));
            
            // Keep only last 5 backups
            const backups = Object.keys(localStorage).filter(key => key.startsWith('w3ll_mailer_backup_'));
            if (backups.length > 5) {
                backups.sort();
                localStorage.removeItem(backups[0]);
            }
        }
        
        // Auto-backup every 5 minutes
        setInterval(backupFormData, 5 * 60 * 1000);
        
        // Connection status indicator
        function updateConnectionStatus() {
            const indicator = document.createElement('div');
            indicator.id = 'connectionStatus';
            indicator.style.cssText = `
                position: fixed;
                top: 80px;
                right: 20px;
                padding: 0.5rem 1rem;
                border-radius: 20px;
                font-family: 'Orbitron', monospace;
                font-size: 0.8rem;
                font-weight: bold;
                z-index: 1000;
                transition: all 0.3s ease;
            `;
            
            if (navigator.onLine) {
                indicator.style.background = 'rgba(0, 255, 136, 0.2)';
                indicator.style.border = '1px solid var(--cyber-primary)';
                indicator.style.color = 'var(--cyber-primary)';
                indicator.innerHTML = '<i class="fas fa-wifi"></i> ONLINE';
            } else {
                indicator.style.background = 'rgba(255, 51, 51, 0.2)';
                indicator.style.border = '1px solid var(--cyber-red)';
                indicator.style.color = 'var(--cyber-red)';
                indicator.innerHTML = '<i class="fas fa-wifi-slash"></i> OFFLINE';
            }
            
            document.body.appendChild(indicator);
            
            // Remove after 3 seconds
            setTimeout(() => {
                indicator.style.opacity = '0';
                setTimeout(() => indicator.remove(), 300);
            }, 3000);
        }
        
        // Monitor connection status
        window.addEventListener('online', updateConnectionStatus);
        window.addEventListener('offline', updateConnectionStatus);
        
        // Initial connection check
        document.addEventListener('DOMContentLoaded', updateConnectionStatus);
    </script>
</body>
</html>