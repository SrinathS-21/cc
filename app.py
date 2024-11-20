import streamlit as st

# Detailed content for all topics
topics = {
    "1. EC2 Instance Creation": """
        ### Step-by-Step Guide to Creating an EC2 Instance

        1. **Log in to AWS Management Console**:
           - Navigate to [AWS Management Console](https://aws.amazon.com/console/).
           - Access the EC2 Dashboard under the "Compute" section.

        2. **Launch an Instance**:
           - Click on the **Launch Instance** button.
           - Provide a descriptive name for your instance.

        3. **Select an Amazon Machine Image (AMI)**:
           - Choose a pre-configured template (e.g., Amazon Linux 2, Ubuntu 20.04).
           - AMIs determine the operating system and pre-installed software.

        4. **Choose an Instance Type**:
           - Select an appropriate type, such as `t2.micro` for free tier eligibility.
           - Instance types differ in CPU, memory, and storage capabilities.

        5. **Configure Instance Details**:
           - Assign or create a key pair for SSH access.
           - Select a VPC and subnet for networking.
           - Configure advanced settings (e.g., IAM roles, shutdown behavior).

        6. **Add Storage**:
           - Define the root volume size (default: 8 GiB General Purpose SSD).
           - Add additional volumes if needed.

        7. **Configure Security Groups**:
           - Create or modify a security group.
           - Open required ports like `22` for SSH and `80` for HTTP.

        8. **Review and Launch**:
           - Review all the settings for correctness.
           - Click **Launch Instance** to start provisioning.

        9. **Connect to the Instance**:
           - Use the public IP address to connect via SSH:
           ```bash
           ssh -i "your-key.pem" ec2-user@<public-ip>
           ```
    """,
    "2. Connect EC2 with RDS": """
        ### Connecting an EC2 Instance to an RDS Database

        1. **Create an RDS Instance**:
           - Go to the RDS Dashboard and click **Create Database**.
           - Choose **Standard Create**, select MySQL, and configure the DB instance settings:
             - Instance type: db.t3.micro (free tier).
             - Storage: General Purpose SSD.
             - Set a username and password.

        2. **Modify RDS Security Group**:
           - Edit the inbound rules of the RDS security group.
           - Add a rule to allow MySQL (port 3306) from your EC2 instance's security group.

        3. **Install MySQL Client on EC2**:
           - SSH into the EC2 instance.
           - Install MySQL client:
           ```bash
           sudo yum install mysql -y
           ```

        4. **Connect EC2 to RDS**:
           - Use the MySQL client to connect:
           ```bash
           mysql -h <RDS-endpoint> -u <username> -p
           ```
           - Provide the RDS password when prompted.
    """,
    "3. Create S3 Bucket and Display Image on Website": """
        ### Steps to Create an S3 Bucket and Display an Image on a Website

        1. **Create an S3 Bucket**:
           - Navigate to the S3 Dashboard and click **Create Bucket**.
           - Provide a unique bucket name and choose a region.
           - Disable block public access if the bucket is for public content.

        2. **Upload Files**:
           - Open the bucket and click **Upload** to add files like images.

        3. **Enable Static Website Hosting**:
           - Go to the bucket's **Properties** tab.
           - Enable static website hosting and specify an index document (e.g., index.html).

        4. **Set Permissions**:
           - Update the bucket policy to allow public access:
           ```json
           {
             "Version": "2012-10-17",
             "Statement": [
               {
                 "Effect": "Allow",
                 "Principal": "*",
                 "Action": "s3:GetObject",
                 "Resource": "arn:aws:s3:::your-bucket-name/*"
               }
             ]
           }
           ```

        5. **Integrate with a Website**:
           - Use the bucket's endpoint URL to serve files.
           - Example HTML to display an image:
           ```html
           <img src="https://your-bucket-name.s3.amazonaws.com/image.jpg" alt="S3 Image">
           ```
    """,
    "4. Create EC2 and Provide Auto Scaling": """
        ### Steps to Set Up Auto Scaling for an EC2 Instance

        1. **Create an EC2 Instance**:
           - Refer to "1. EC2 Instance Creation".

        2. **Set Up Auto Scaling**:
           - Go to the **Auto Scaling Groups** section in the EC2 Dashboard.
           - Create a new Auto Scaling group and associate it with your EC2 instance.

        3. **Define Scaling Policies**:
           - Add a policy to increase or decrease instances based on metrics like CPU utilization.
           - Example: Add an instance if CPU > 70%, remove if CPU < 30%.

        4. **Test Auto Scaling**:
           - Simulate load to verify scaling behavior.
    """,
    "5. Create VPC and Provide Network Settings": """
        ### Steps to Create a VPC and Configure Networking

        1. **Create a VPC**:
           - Go to the VPC Dashboard and click **Create VPC**.
           - Specify a CIDR block (e.g., 10.0.0.0/16).

        2. **Create Subnets**:
           - Create public and private subnets within the VPC.
           - Assign CIDR blocks (e.g., 10.0.1.0/24 for public).

        3. **Add an Internet Gateway**:
           - Attach the gateway to your VPC for internet access.

        4. **Configure Route Tables**:
           - Create and associate route tables for public and private subnets.
           - Add routes to the internet gateway for public subnets.

        5. **Test Connectivity**:
           - Launch an instance in the public subnet and verify internet access.
    """,
    "6. Launch MySQL in RDS": """
        ### Launching a MySQL Instance in Amazon RDS

        1. **Navigate to RDS**:
           - Open the RDS Dashboard and click **Create Database**.
           - Choose MySQL as the database engine.

        2. **Configure Database Settings**:
           - Select Standard Create.
           - Specify instance size, storage type, and credentials.

        3. **Assign Networking Settings**:
           - Place the RDS instance in a VPC.
           - Ensure the security group allows MySQL connections (port 3306).

        4. **Connect to the Database**:
           - SSH into an EC2 instance with MySQL installed and connect:
           ```bash
           mysql -h <RDS-endpoint> -u <username> -p
           ```
    """,
    "7. Create IAM Role to Access an S3 Bucket": """
        ### Steps to Create an IAM Role for S3 Access

        1. **Create an IAM Role**:
           - Navigate to IAM Roles and click **Create Role**.
           - Select **AWS Service** and choose EC2.

        2. **Attach S3 Policy**:
           - Add the policy `AmazonS3FullAccess` (or create a custom policy).

        3. **Attach the Role to EC2**:
           - Go to your EC2 instance, click **Actions > Security > Modify IAM Role**, and attach the created role.

        4. **Test Access**:
           - Use AWS CLI on the EC2 instance to test access:
           ```bash
           aws s3 ls s3://your-bucket-name
           ```
    """
}

# Streamlit UI
st.title("AWS Practical Guide")
st.sidebar.title("Topics")
selected_topic = st.sidebar.selectbox("Select a topic to view", list(topics.keys()))

st.header(selected_topic)
st.markdown(topics[selected_topic])
