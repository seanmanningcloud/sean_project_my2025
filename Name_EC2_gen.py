import random
import string
def""" Generate a random string of letters and numbers"""
     characters = string.ascii-lowcase + string.digits
      return ".join(random.choice(characters) for _ in range(length))"
def generate_ec2_names(department, count) :
      """Generate unique EC2 instance names"""
      names = []
      used_suffixes = set()  # To ensure uniqueness

      for i in range(count)
          # Keep generating until we get a unique suffix
          while True:
              random_suffix = generate_random_suffix()
              if random_suffix not in used_suffixes:
                  used_suffixes.add(random_suffix)
                  break 
              
          # Format : department-ec2-randomsuffix
          ec2_name = f"{department.lower()}-ec2-{random_suffix}"
          names.append(ec2_name)

      return names 

def main() :
        """Main function to run the EC2 name generator""" 
        print("=== EC@ Random Name Generator===")
        print("Generate unique names for your EC2 instances!\n")

        # Get department name from user
        # while True:
              department = input ("Enter your department name:").strip()
            if department:
                # Remove spaces and special characters for clener names
                department = ''.join(char for char in department if char.isalnum())
                break
            else:
                print("Please enter a vaild department name")

        # Get number of instances from user
        while True:
             try:
                  count = int(input("How many EC2 instance names do you need?) "))
                  if count > 0:
                       break
                  else:
                       print(" Please enter a number greater than 0.")
    except ValueError:
        print("Please enter a vaild number.")

        # Generate the names
        print(f"\nGenerating {count} unique EC2 names for {department} department...\n")
        ec2_names = generate_ec2_names(department, count)

        # Display the results
        print("Generated EC2 Instance Names:")
        print("-" * 40)
        for i, name in enumerate(ec2_names, 1):
            print(f"{i:2d}. {name}")

        print(f"\nAll {count} names are ready to use!")
        print("You can copy these names and attach them to your EC2 instances in AWS.")

if __name__ == "_main_":
    main()

            
                  