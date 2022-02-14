## J+M+J

# Project 2 - Robert Green

## Part 1:

### 1.
This is the kind of container in which all instances and networks are housed inside of.
![VPC pic](./pictures/vpc-screenshot.PNG)

### 2.
This is the network in which my VPC will operate.
![subnet pic](./pictures/subnet-screenshot.PNG))

### 3.
This is the virtual device that acts as a router and is the doorway from the public network to the private and vise-versa.
![gateway pic](./pictures/gw-screenshot.PNG)

### 4.
This is a table that shows what packets should be routed where within the network.
![route table pic](./pictures/routetable-screenshot.PNG)

### 5.
This is a rule set that specifies what other machines are allowed to talk to this network.
![security group pic](./pictures/securityGroup-screenshot.PNG))

### 6. 
(Used keypair already in existance)


## Part 2:

### 1. 
Selected: Amazon Linux 2 AMI (HVM) - Kernel 5.10

Default Username: ec2-user

### 2. 
I selected the vpc in the 'Network' choice, which automatically filled in the other needed blanks (such as Subnet).

### 3. 
It will not be auto-assigned. This way it cannot change without my knowledge and I will always be able to use the same ip to access my vpc.

### 4. 
I added a new volume by the setup screen's 'Add New Volume' button.

### 5. 
Selecting the 'Add Tags' page, I clicked 'Click to Add Tag' in the setup menu

### 6. 
Selecting the 'Configure Security Group' page, I chose 'Select an existing security group' and selected my pre-made group.

### 7. 
Selecting the 'Elastic IPs' on the sidebar, I clicked 'Allocate Elastic IP address'. Once the ip was allocated, I chose 'Associate Elastic IP address' from the dropdown menu under 'Actions' and selected my EC2.

### 8. 
![instance pic](./pictures/instanceDetails-screenshot.PNG)

### 9. 
Used the command 'ssh -i ceg-3120-aws.pem ec2-user@52.1.232.41' to ssh into the instance. I then used 'sudo hostname Green-amazonKernel'.

### 10. 
![ssh'ed in pic](./pictures/Connection-screenshot.PNG)
