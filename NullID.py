#!/usr/bin/env python3

import uuid
import random
import string
from datetime import datetime, timedelta
import time
import sys

# Function to simulate slow typing for a cool effect
def slow_type(text, delay=0.05):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()  # New line after the text is finished

# Function to print the introductory message
def print_intro():
    text = "Bild By Iraqi Shadow ( IRAQI BLACK HAT TEAM )"
    slow_type(text, delay=0.07)
    print()

# List of countries with expanded data, including IP prefixes
COUNTRIES = [
    {"name": "USA", "phone_code": "+1", "email_domain": "mail.com", "iban_country": "US", "ip_prefix": ["172.", "192.", "10."]},
    {"name": "Germany", "phone_code": "+49", "email_domain": "gmx.de", "iban_country": "DE", "ip_prefix": ["80.", "90.", "141."]},
    {"name": "France", "phone_code": "+33", "email_domain": "orange.fr", "iban_country": "FR", "ip_prefix": ["88.", "92.", "178."]},
    {"name": "Russia", "phone_code": "+7", "email_domain": "mail.ru", "iban_country": "RU", "ip_prefix": ["95.", "178.", "46."]},
    {"name": "Italy", "phone_code": "+39", "email_domain": "libero.it", "iban_country": "IT", "ip_prefix": ["79.", "87.", "93."]},
    {"name": "Japan", "phone_code": "+81", "email_domain": "yahoo.co.jp", "iban_country": "JP", "ip_prefix": ["118.", "122.", "210."]},
    {"name": "Brazil", "phone_code": "+55", "email_domain": "uol.com.br", "iban_country": "BR", "ip_prefix": ["177.", "187.", "200."]},
    {"name": "India", "phone_code": "+91", "email_domain": "rediffmail.com", "iban_country": "IN", "ip_prefix": ["103.", "106.", "157."]},
    {"name": "Canada", "phone_code": "+1", "email_domain": "gmail.com", "iban_country": "CA", "ip_prefix": ["24.", "64.", "70."]},
    {"name": "UK", "phone_code": "+44", "email_domain": "hotmail.co.uk", "iban_country": "GB", "ip_prefix": ["51.", "81.", "86."]},
    {"name": "Australia", "phone_code": "+61", "email_domain": "hotmail.com.au", "iban_country": "AU", "ip_prefix": ["101.", "139.", "203."]},
    {"name": "Spain", "phone_code": "+34", "email_domain": "telefonica.net", "iban_country": "ES", "ip_prefix": ["151.", "188.", "212."]},
    {"name": "Netherlands", "phone_code": "+31", "email_domain": "gmail.com", "iban_country": "NL", "ip_prefix": ["77.", "94.", "145."]},
    {"name": "South Korea", "phone_code": "+82", "email_domain": "hanmail.net", "iban_country": "KR", "ip_prefix": ["112.", "121.", "211."]},
    {"name": "Mexico", "phone_code": "+52", "email_domain": "prodigy.net.mx", "iban_country": "MX", "ip_prefix": ["187.", "201.", "189."]},
    {"name": "Argentina", "phone_code": "+54", "email_domain": "arnet.com.ar", "iban_country": "AR", "ip_prefix": ["181.", "190.", "200."]},
    {"name": "Sweden", "phone_code": "+46", "email_domain": "telia.com", "iban_country": "SE", "ip_prefix": ["83.", "90.", "193."]},
    {"name": "Norway", "phone_code": "+47", "email_domain": "online.no", "iban_country": "NO", "ip_prefix": ["80.", "91.", "188."]},
    {"name": "Finland", "phone_code": "+358", "email_domain": "luukku.com", "iban_country": "FI", "ip_prefix": ["62.", "84.", "88."]},
    {"name": "Poland", "phone_code": "+48", "email_domain": "wp.pl", "iban_country": "PL", "ip_prefix": ["89.", "194.", "213."]}
]

# Expanded lists for more diverse identity generation
FIRST_NAMES = ["James", "Maria", "Liam", "Noah", "Emma", "Olivia", "Ethan", "Ava", "Sophia", "Isabella", "Jackson", "Lucas", "Aiden", "Riley", "Chloe", "Zoe", "Mila", "Harper", "Logan", "Grace", "Oliver", "Elijah", "Charlotte", "Amelia", "Benjamin", "Lucas", "Mia", "Evelyn"]
LAST_NAMES = ["Smith", "Johnson", "Williams", "Brown", "Jones", "Garcia", "Davis", "Miller", "Rodriguez", "Martinez", "Hernandez", "Lopez", "Gonzalez", "Wilson", "Anderson", "Thomas", "Taylor", "Moore", "Jackson", "White", "Harris", "Clark", "Lewis", "Robinson", "Walker"]
JOBS = ["Penetration Tester", "Software Engineer", "Network Analyst", "Data Scientist", "Security Auditor", "Red Teamer", "Cybersecurity Consultant", "Cloud Architect", "DevOps Engineer", "Machine Learning Engineer", "System Administrator", "IT Manager", "Database Administrator"]
BANKS = ["CyberBank", "Redline Bank", "Phantom Bank", "ZeroDay Bank", "Secure Digital Bank", "Global Cyber Trust", "DarkNet Finance", "Stealth Wealth Bank"]
UNIVERSITIES = ["State University", "Technical Institute", "Global College", "Research Academy", "Advanced School of Tech", "National University", "Metropolitan University", "Central Institute of Science"]
DEGREES = ["Bachelor of Science", "Master of Arts", "PhD in Computer Science", "Associate Degree", "Master of Business Administration", "Doctor of Engineering"]
MAJORS = ["Computer Science", "Cyber Security", "Network Engineering", "Data Science", "Software Engineering", "Information Technology", "Artificial Intelligence", "Business Administration", "Electrical Engineering", "Applied Mathematics"]
COMPANIES = ["TechSolutions Inc.", "Global Cyber Corp", "SecureNet Ltd.", "Innovate Labs", "Digital Forge", "Quantum Systems", "Apex Innovations", "Synergy Tech Solutions", "Pinnacle Software"]

# Generates a random lowercase string of a given length
def random_string(length=8):
    return ''.join(random.choices(string.ascii_lowercase, k=length))

# Generates a strong password, potentially incorporating parts of name or birth year
def strong_password(full_name, birthdate_str, length=16):
    chars = string.ascii_letters + string.digits + string.punctuation
    name_part = "".join(filter(str.isalnum, full_name)).lower()
    birth_year = birthdate_str.split('-')[0]
    
    while True:
        pwd = ''.join(random.choice(chars) for _ in range(length))
        
        # Try to insert part of the name
        if len(name_part) >= 4:
            if random.random() < 0.3: # 30% chance to insert
                insert_len = random.randint(3,min(len(name_part), 5))
                insert_pos = random.randint(0, len(pwd) - insert_len)
                pwd = pwd[:insert_pos] + name_part[:insert_len] + pwd[insert_pos + insert_len:]
        
        # Try to insert birth year
        if random.random() < 0.2: # 20% chance to insert
            insert_pos = random.randint(0, len(pwd) - len(birth_year))
            pwd = pwd[:insert_pos] + birth_year + pwd[insert_pos + len(birth_year):]

        # Ensure the password meets strength criteria and length
        if (any(c.islower() for c in pwd) and any(c.isupper() for c in pwd)
            and any(c.isdigit() for c in pwd) and any(c in string.punctuation for c in pwd)
            and len(pwd) >= length):
            return pwd[:length] # Trim to original length if it grew too long

# Generates a fake Social Security Number (SSN)
def generate_ssn():
    return f"{random.randint(100,999)}-{random.randint(10,99)}-{random.randint(1000,9999)}"

# Generates fake credit card details
def generate_credit_card():
    num = "".join(str(random.randint(0,9)) for _ in range(16))
    exp = f"{random.randint(1,12):02d}/{random.randint(25,30)}"
    cvv = f"{random.randint(100,999)}"
    return num, exp, cvv

# Generates fake GPS coordinates
def generate_gps():
    lat = round(random.uniform(-90.0, 90.0), 6)
    lon = round(random.uniform(-180.0, 180.0), 6)
    return f"{lat} N, {lon} E"

# Generates a fake IBAN (International Bank Account Number)
def generate_iban(country_code):
    check_digits = str(random.randint(10, 99))
    bban = ''.join(random.choices(string.ascii_uppercase + string.digits, k=16))
    return f"{country_code}{check_digits}{bban}"

# Generates a somewhat logical IP address based on country prefixes
def generate_ip_address(country_ip_prefixes):
    prefix = random.choice(country_ip_prefixes)
    return f"{prefix}{random.randint(1,254)}.{random.randint(1,254)}.{random.randint(1,254)}"

# Generates a fake MAC address
def generate_mac_address():
    return ':'.join(['{:02x}'.format(random.randint(0x00, 0xff)) for _ in range(6)]).upper()
    # Generates a fake Device ID
def generate_device_id():
    return str(uuid.uuid4()).upper()

# Generates a simple biometric hash
def generate_biometric_hash(uuid_val, full_name):
    combined_string = f"{uuid_val}-{full_name}-biometric_salt"
    return uuid.uuid5(uuid.NAMESPACE_URL, combined_string).hex

# Generates a realistic education history
def generate_education_history(birthdate_str):
    edu_history = []
    
    birth_year = int(birthdate_str.split('-')[0])
    high_school_grad_year = birth_year + 18
    
    edu_history.append({
        "Degree": "High School Diploma",
        "Major": "General Studies",
        "Institution": f"{random_string(7).title()} High School",
        "Years": f"{high_school_grad_year - 4}-{high_school_grad_year}"
    })
    
    if random.random() < 0.9: # 90% chance for higher education
        uni_start_year = high_school_grad_year + random.randint(0, 2)
        degree = random.choice(DEGREES)
        major = random.choice(MAJORS)
        
        if "Bachelor" in degree:
            uni_end_year = uni_start_year + 4
        elif "Master" in degree:
            uni_end_year = uni_start_year + 2
        elif "PhD" in degree:
            uni_end_year = uni_start_year + 4
        else: # Associate Degree
            uni_end_year = uni_start_year + 2

        if uni_end_year <= datetime.now().year + 1: # Ensure it's not too far in the future
            edu_history.append({
                "Degree": degree,
                "Major": major,
                "Institution": f"{random.choice(UNIVERSITIES)}",
                "Years": f"{uni_start_year}-{uni_end_year}"
            })

    if random.random() < 0.2 and len(edu_history) > 1: # 20% chance for a second degree
        prev_end_year = int(edu_history[-1]["Years"].split('-')[1])
        if datetime.now().year - prev_end_year > 2:
            next_start_year = prev_end_year + random.randint(1, 3)
            degree = random.choice(DEGREES)
            major = random.choice(MAJORS)
            if "Master" in degree:
                next_end_year = next_start_year + 2
            elif "PhD" in degree:
                next_end_year = next_start_year + 4
            else:
                next_end_year = next_start_year + 2
            
            if next_end_year <= datetime.now().year + 1:
                 edu_history.append({
                    "Degree": degree,
                    "Major": major,
                    "Institution": f"{random.choice(UNIVERSITIES)}",
                    "Years": f"{next_start_year}-{next_end_year}"
                })
    return edu_history

# Generates a fake employment history
def generate_employment_history(birthdate_str):
    emp_history = []
    
    birth_year = int(birthdate_str.split('-')[0])
    first_job_year = birth_year + random.randint(20, 24) # First job typically after college
    
    current_year = datetime.now().year
    
    num_jobs = random.randint(1, 3) # 1 to 3 jobs

    for i in range(num_jobs):
        company = random.choice(COMPANIES)
        job_title = random.choice(JOBS)
        
        if i == 0:
            start_year = first_job_year
        else:
            prev_end_year = int(emp_history[-1]["End Date"].split('-')[0]) if emp_history[-1]["End Date"] != "Present" else current_year
            start_year = prev_end_year + random.randint(0, 2) # Gap between jobs
            
        if start_year > current_year: # Avoid future start dates for past jobs
            start_year = current_year - random.randint(1,5)

        end_date = "Present"
        if i < num_jobs - 1: # If not the current job
            end_year = start_year + random.randint(1, 5) # Job duration 1 to 5 years
            if end_year < current_year:
                end_date = f"{end_year}-{random.randint(1,12):02d}-{random.randint(1,28):02d}"
            else:
                end_date = "Present" # If the calculated end date is in the future, it's the current job
                
        # Ensure start year is before or same as end year (if not 'Present')
        if end_date != "Present" and int(end_date.split('-')[0]) < start_year:
            end_date = "Present"

        emp_history.append({
            "Company": company,
            "Job Title": job_title,
            "Start Date": f"{start_year}-{random.randint(1,12):02d}-{random.randint(1,28):02d}",
            "End Date": end_date
        })
    return emp_history

# Generates a fake activity log
def generate_activity_log(username):
    logs = []
    num_logs = random.randint(3, 7)
    
    current_time = datetime.now()
    
    for _ in range(num_logs):
        action_type = random.choice(["Login Attempt", "Password Change", "Account Update", "Transaction", "File Access", "Login Success"])
        device = random.choice(["Mobile", "Desktop", "Tablet"])
        ip = ".".join(map(str, (random.randint(0, 255) for _ in range(4))))
        
        time_offset = timedelta(days=random.randint(0, 365), hours=random.randint(0, 23), minutes=random.randint(0, 59))
        log_time = (current_time - time_offset).strftime("%Y-%m-%d %H:%M:%S")
        
        log_entry = {
            "Timestamp": log_time,
            "Action": action_type,
            "User": username,
            "Device": device,
            "IP Address": ip
        }
        logs.append(log_entry)
        
    return logs

# Main function to generate a fake identity
def generate_identity(country, is_parent=False, birthdate_override=None, gender_override=None):
    uid = str(uuid.uuid4())
    
    if gender_override:
        gender = gender_override
    else:
        gender = random.choice(["Male", "Female"])

    # Select names based on gender to make it more realistic
    male_names = [n for n in FIRST_NAMES if n not in ["Maria", "Emma", "Olivia", "Ava", "Sophia", "Isabella", "Riley", "Chloe", "Zoe", "Mila", "Harper", "Grace", "Charlotte", "Amelia", "Mia", "Evelyn"]]
    female_names = [n for n in FIRST_NAMES if n not in ["James", "Liam", "Noah", "Ethan", "Jackson", "Lucas", "Aiden", "Logan", "Oliver", "Elijah", "Benjamin"]]

    if gender == "Male":
        first = random.choice(male_names)
    else:
        first = random.choice(female_names)

    last = random.choice(LAST_NAMES)
    full_name = f"{first} {last}"
    
    if birthdate_override:
        birthdate_dt = birthdate_override
        age = datetime.now().year - birthdate_dt.year
    else:
        age = random.randint(20, 45) if not is_parent else random.randint(30, 60)
        birth_year = datetime.now().year - age
        birthdate_dt = datetime.now().replace(year=birth_year, month=random.randint(1,12), day=random.randint(1,28))
    
    birthdate = birthdate_dt.strftime("%Y-%m-%d")

    email = f"{first.lower()}.{last.lower()}{random.randint(100,999)}@{country['email_domain']}"
    username = f"{first.lower()}{random.randint(1000,9999)}"
    password = strong_password(full_name, birthdate)
    phone = f"{country['phone_code']}-{random.randint(100,999)}-{random.randint(100,999)}-{random.randint(1000,9999)}"
    marital_status = random.choice(["Single", "Married", "Divorced"])
    children = random.randint(0, 3) if marital_status != "Single" else 0
    job = random.choice(JOBS)
    
    address = f"{random.randint(100,9999)} {random_string(5).title()} Street, {random_string(6).title()}"
    gps = generate_gps()
    ssn = generate_ssn()
    credit_num, credit_exp, credit_cvv = generate_credit_card()
    bank = random.choice(BANKS)
    iban = generate_iban(country['iban_country'])
    
    ip_address = generate_ip_address(country['ip_prefix'])
    os_list = ["Windows 10", "Windows 11", "macOS Ventura", "macOS Sonoma", "Ubuntu Linux", "Android 14", "iOS 17"]
    device_type = random.choice(["Desktop", "Laptop", "Smartphone", "Tablet"])
    operating_system = random.choice(os_list)
    mac_address = generate_mac_address()
    device_id = generate_device_id()

    biometric_hash = generate_biometric_hash(uid, full_name)
    activity_log = generate_activity_log(username)
    education_history = generate_education_history(birthdate)
    employment_history = generate_employment_history(birthdate)
    
    identity = {
        "UUID": uid,"Full Name": full_name,
        "Gender": gender,
        "Age": age,
        "Birthdate": birthdate,
        "Email": email,
        "Username": username,
        "Password": password,
        "Phone": phone,
        "Marital Status": marital_status,
        "Children": children,
        "Job": job,
        "Address": address,
        "GPS Coordinates": gps,
        "SSN": ssn,
        "Credit Card": {
            "Number": credit_num,
            "Expiry": credit_exp,
            "CVV": credit_cvv
        },
        "Bank": bank,
        "IBAN": iban,
        "IP Address": ip_address,
        "Device Info": {
            "Type": device_type,
            "OS": operating_system,
            "MAC Address": mac_address,
            "Device ID": device_id
        },
        "Biometric Hash": biometric_hash,
        "Activity Log": activity_log,
        "Education History": education_history,
        "Employment History": employment_history
    }

    return identity

# Function to choose a country
def choose_country():
    print("\nChoose a country from the list below by typing its number:")
    print("Or type 'R' to generate an identity from a random country.")
    print("-" * 40)
    for i, c in enumerate(COUNTRIES, 1):
        slow_type(f"{i}. {c['name']}", delay=0.01)
    print("-" * 40)

    while True:
        try:
            choice_input = input("Your choice: ").strip().upper()
            if choice_input == 'R':
                return random.choice(COUNTRIES)
            
            choice = int(choice_input)
            if 1 <= choice <= len(COUNTRIES):
                return COUNTRIES[choice - 1]
            else:
                print("Invalid choice. Please try again.")
        except ValueError:
            print("Please enter a valid number or 'R'.")

# Function to display a real-time progress bar
def progress_bar(iteration, total, prefix='', suffix='', decimals=1, length=50, fill='█', print_end='\r'):
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filled_length = int(length * iteration // total)
    bar = fill * filled_length + '-' * (length - filled_length)
    sys.stdout.write(f'\r{prefix} |{bar}| {percent}% {suffix}')
    sys.stdout.flush()
    if iteration == total:
        sys.stdout.write('\n')

# Main execution logic
def main():
    try:
        print_intro()
        while True:
            country = choose_country()
            slow_type(f"\nGenerating fake identity for {country['name']}...\n", delay=0.04)
            
            steps = 10 # Total steps for the progress bar
            
            # Step 1: Generate basic identity details
            progress_bar(1, steps, prefix='Gathering core data...', suffix='In progress')
            identity = generate_identity(country)
            time.sleep(0.5)

            # Step 2: Preparing device information
            progress_bar(2, steps, prefix='Preparing device info...', suffix='In progress')
            time.sleep(0.3)

            # Step 3: Generating IP Address
            progress_bar(3, steps, prefix='Generating IP Address...', suffix='In progress')
            time.sleep(0.3)

            # Step 4: Crafting Biometric Hash
            progress_bar(4, steps, prefix='Crafting biometric hash...', suffix='In progress')
            time.sleep(0.3)

            # Step 5: Building Education History
            progress_bar(5, steps, prefix='Building education history...', suffix='In progress')
            time.sleep(0.3)

            # Step 6: Compiling Employment History
            progress_bar(6, steps, prefix='Compiling employment history...', suffix='In progress')
            time.sleep(0.3)
            
            # Step 7: Assembling Activity Log
            progress_bar(7, steps, prefix='Assembling activity log...', suffix='In progress')
            time.sleep(0.3)

            # Step 8: Securing Password
            progress_bar(8, steps, prefix='Securing password...', suffix='In progress')
            time.sleep(0.3)

            # Step 9: Performing Data Integrity Check
            progress_bar(9, steps, prefix='Performing data integrity check...', suffix='In progress')
            time.sleep(0.3)

            progress_bar(steps, steps, prefix='Identity generated successfully!', suffix='Completed')
            time.sleep(0.5)
            print("\n") # New line after progress bar

            # Print generated identity details
            for key, value in identity.items():
                if isinstance(value, dict):
                    slow_type(f"{key}:", delay=0.01)
                    for k, v in value.items():
                        slow_type(f"  {k}: {v}", delay=0.005)
                elif isinstance(value, list):
                    slow_type(f"{key}:", delay=0.01)
                    if key == "Activity Log":
                        for entry in value:
                            slow_type(f"  - {entry['Timestamp']} | {entry['Action']} by {entry['User']} on {entry['Device']} from {entry['IP Address']}", delay=0.003)
                    elif key == "Education History" or key == "Employment History":
                        for item in value:
                            item_str = ", ".join([f"{k}: {v}" for k, v in item.items()])
                            slow_type(f"  - {item_str}", delay=0.003)
                    else:
                        slow_type(f"  {', '.join(value)}", delay=0.005)
                else:
                    slow_type(f"{key}: {value}", delay=0.005)
            
            # Ask to generate a family
            slow_type("\n-------------------------------------------", delay=0.01)
            slow_type("Do you want to generate a family for this identity? (Y/N)", delay=0.03)
            create_family = input("Your choice: ").strip().upper()
            if create_family == 'Y':
                slow_type("\nGenerating family details...", delay=0.04)
                
                father_birthdate = datetime.strptime(identity["Birthdate"], "%Y-%m-%d")
                
                # Mother's age is typically slightly younger than the father's
                mother_birthdate = father_birthdate + timedelta(days=random.randint(365, 5 * 365)) 
                if mother_birthdate > datetime.now(): # Ensure mother isn't born in the future
                    mother_birthdate = father_birthdate - timedelta(days=random.randint(365, 5 * 365))

                mother_identity = generate_identity(country, is_parent=True, birthdate_override=mother_birthdate, gender_override="Female")
                
                print("\n\n-------------------------------------------")
                slow_type("Mother's Information:", delay=0.05)
                print("-------------------------------------------")
                for key, value in mother_identity.items():
                    if isinstance(value, dict):
                        slow_type(f"{key}:", delay=0.01)
                        for k, v in value.items():
                            slow_type(f"  {k}: {v}", delay=0.005)
                    elif isinstance(value, list):
                        slow_type(f"{key}:", delay=0.01)
                        if key == "Activity Log":
                            for entry in value:
                                slow_type(f"  - {entry['Timestamp']} | {entry['Action']} by {entry['User']} on {entry['Device']} from {entry['IP Address']}", delay=0.003)
                        elif key == "Education History" or key == "Employment History":
                            for item in value:
                                item_str = ", ".join([f"{k}: {v}" for k, v in item.items()])
                                slow_type(f"  - {item_str}", delay=0.003)
                        else:
                            slow_type(f"  {', '.join(value)}", delay=0.005)
                    else:
                        slow_type(f"{key}: {value}", delay=0.005)
                
                num_children = random.randint(1, 5)
                print(f"\n\n-------------------------------------------")
                slow_type(f"Generating {num_children} children's information:", delay=0.05)
                print("-------------------------------------------")

                for i in range(num_children):
                    child_gender = random.choice(["Male", "Female"])
                    # Child's age is younger than mother's, and at least 0 years old
                    # Ensure child is born after mother and before current date
                    max_child_age_days = (datetime.now() - mother_birthdate).days - (365 * 2) # At least 2 years difference
                    if max_child_age_days < 0: # If mother is too young to have children
                        child_birthdate = mother_birthdate + timedelta(days=365*2) # Default to 2 years after mother
                    else:
                        child_birthdate = mother_birthdate + timedelta(days=random.randint(365*2, max_child_age_days))
                    
                    # Cap child's age at 18 for basic info
                    if datetime.now().year - child_birthdate.year > 18:
                        child_birthdate = datetime.now() - timedelta(days=random.randint(1*365, 18*365))


                    child_first_name = random.choice(FIRST_NAMES)
                    child_last_name = identity["Full Name"].split(" ")[-1] # Inherit last name from primary identity

                    child_age = datetime.now().year - child_birthdate.year
                    
                    child_info = {
                        "Full Name": f"{child_first_name} {child_last_name}",
                        "Gender": child_gender,
                        "Age": child_age,
                        "Birthdate": child_birthdate.strftime("%Y-%m-%d")
                    }
                    slow_type(f"\nChild {i+1} Information:", delay=0.03)
                    for k, v in child_info.items():
                        slow_type(f"  {k}: {v}", delay=0.005)

            # Ask to generate another identity
            slow_type("\n-------------------------------------------", delay=0.01)
            slow_type("Do you want to generate a new identity? (Y/N)", delay=0.03)
            answer = input("Your choice: ").strip().upper()
            if answer != 'Y':
                slow_type("Exiting... Talk Good about owr tool !", delay=0.05)
                break # Exit the loop and end the program

    except KeyboardInterrupt:
        print("\n\nExiting... Talk Good about owr tool !")
        sys.exit(0)
    except Exception as e:
        print(f"\nAn error occurred: {e}")
        print("Please try again or contact support if the issue persists.")
        sys.exit(1)

if __name__ == "__main__":
    main()
