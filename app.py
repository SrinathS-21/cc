import streamlit as st

# Content for each topic
topics = {
    "1. EC2 Instance Creation": """
        1. **Log in to AWS Console**:
           - Navigate to the EC2 Dashboard.
        
        2. **Launch an Instance**:
           - Click on **Launch Instance**.
           - Provide a name for your instance.
        
        3. **Select an AMI**:
           - Choose an Amazon Machine Image (e.g., Amazon Linux 2 or Ubuntu).
        
        4. **Choose an Instance Type**:
           - Select the type (e.g., t2.micro for free tier).
        
        5. **Configure Instance**:
           - Assign a key pair for SSH access.
           - Configure network settings, such as selecting an existing VPC and subnet.
        
        6. **Add Storage**:
           - Specify the size and type of the root volume (e.g., 8 GiB General Purpose SSD).
        
        7. **Configure Security Groups**:
           - Create or use an existing security group.
           - Open necessary ports (e.g., 22 for SSH, 80 for HTTP).
        
        8. **Launch Instance**:
           - Review settings and click **Launch Instance**.
        
        9. **Connect to the Instance**:
           - Use SSH to connect:
           ```bash
           ssh -i "your-key.pem" ec2-user@<public-ip>
           ```
    """,
    "2. Connect EC2 with RDS": """
        1. **Create RDS Instance**:
           - In the RDS Dashboard, launch a new RDS instance with MySQL.
           - Ensure it is in the same VPC as your EC2 instance.
        
        2. **Modify Security Group for RDS**:
           - Add a rule to allow inbound MySQL (port 3306) from the EC2 instance's security group.
        
        3. **Install MySQL Client on EC2**:
           - Connect to EC2 and run:
           ```bash
           sudo yum install mysql -y
           ```
        
        4. **Connect to RDS from EC2**:
           - Use the command:
           ```bash
           mysql -h <RDS-endpoint> -u <username> -p
           ```
    """,
    "3. Create S3 Bucket and Display Image on Website": """
        1. **Create an S3 Bucket**:
           - Navigate to the S3 Dashboard and click **Create Bucket**.
           - Name the bucket and select the region.
           - Enable or disable public access as needed.

        2. **Upload Images**:
           - Open the bucket, click **Upload**, and add your image files.

        3. **Enable Static Website Hosting**:
           - Go to the bucket's **Properties** tab.
           - Enable static website hosting and set an index document (e.g., index.html).

        4. **Grant Permissions**:
           - Update the bucket policy to allow public read access (if needed).
           - Example:
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
           - Use the bucket's endpoint URL to display the images in your website code.
    """,
    "4. Create EC2 and Provide Auto Scaling": """
        1. **Launch EC2 Instance**:
           - Follow the steps in "1. EC2 Instance Creation".

        2. **Create an Auto Scaling Group**:
           - Go to the Auto Scaling Groups section.
           - Create a new Auto Scaling Group and attach the EC2 instance.

        3. **Set Scaling Policies**:
           - Define scaling policies based on CPU utilization or other metrics.
           - Example: Add an instance if CPU > 70%, remove if < 20%.

        4. **Test Auto Scaling**:
           - Simulate load to verify the scaling behavior.
    """,
    "5. Create VPC and Provide Network Settings": """
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
        1. **Create a MySQL RDS Instance**:
           - Navigate to the RDS Dashboard and click **Create Database**.
           - Select MySQL and configure settings (DB instance class, storage, username/password).

        2. **Set Security Groups**:
           - Allow MySQL (3306) access from your EC2 instance.

        3. **Connect to the Database**:
           - Install a MySQL client on EC2.
           - Connect using:
           ```bash
           mysql -h <RDS-endpoint> -u <username> -p
           ```
    """,
    "7. Create IAM Role to Access an S3 Bucket": """
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
