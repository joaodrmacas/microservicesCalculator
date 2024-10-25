## Name
Web Calculator

## Description
A calculator app divided in 3 microservices for each operation. 
Project for Administration and Management of IT Infrastructures and Services implementing
Vagrant, Terraform, Ansible and Kubernetes.

# Installation

# Vagrant Commands

1. **Initialize Variables**  
Linux:
   ```bash
   export VAGRANT_VAGRANTFILE="Vagrantfile.vbox"
   ```
   or
   ```bash
   export VAGRANT_VAGRANTFILE="Vagrantfile.docker"
   ```
Windows:
   ```bash
   $env:VAGRANT_VAGRANTFILE = "Vagrantfile.vbox"
   ```
   or
   ```bash
   $env:VAGRANT_VAGRANTFILE = "Vagrantfile.docker"
   ```

2. **Validate Vagrantfile** 
   Validate vagrant.
   ```bash
   vagrant validate
   ```

3. **Intialize Management Node** 
   Intialize VM.
   ```bash
   vagrant up
   ```

4. **Connect to Management Node** 
   SSH connection to VM.
   ```bash
   vagrant ssh mgmt
   ```

## Google Cloud

1. **Change Project ID** 
   In terraform-gcp-variables.tf change  the project ID.
   ```bash
   variable "GCP_PROJECT_ID" {
    default = "<PROJECT-ID>"
   }
   ```

1. **Create Key and change path** 
   Create a key and update the path to the json file.
   ```bash
   provider "google" {
      credentials = file("<PATH_TO_GCP_CREDENTIALS_FILE>")
      project = var.GCP_PROJECT_ID
      zone = var.GCP_ZONE
   }
   ```
## Terraform Commands

**Inside gcpcloud directory** 

1. **Initialize Terraform**  
   Initialize the Terraform configuration.
   ```bash
   terraform init
   ```

2. **Generate SSH Key**  
   Generate a new RSA SSH key pair.
   ```bash
   ssh-keygen -t rsa -b 2048
   ```

3. **Plan Deployment**  
   Generate an execution plan for Terraform.
   ```bash
   terraform plan
   ```

4. **Apply Deployment**  
   Apply the planned changes to your infrastructure.
   ```bash
   terraform apply
   ```

5. **Update Terraform Output**  
   Run a script to update Terraform output values.
   ```bash
   sudo ./update_tf_output.sh
   ```

## Ansible Commands

1. **Configure GCP Nodes**  
   Run the playbook to configure Google Cloud Platform nodes.
   ```bash
   ansible-playbook -i gcphosts ansible-gcp-configure-nodes.yml
   ```

2. **Install Kubernetes**  
   Run the playbook to install Kubernetes on the nodes.
   ```bash
   ansible-playbook -i gcphosts ansible-k8s-install.yml
   ```

5. **Install Monitoring Services (Prometheus, Grafana)**
   Run the playbook to start grafana and prometheus on the cluster.
   ```bash
   ansible-playbook -i gcphosts ansible-monitoring-install.yml
   ```

3. **Create Kubernetes Cluster**  
   Run the playbook to create a Kubernetes cluster.
   ```bash
   ansible-playbook -i gcphosts ansible-create-cluster.yml
   ```

4. **Join Worker Nodes**  
   Run the playbook to join worker nodes to the cluster.
   ```bash
   ansible-playbook -i gcphosts ansible-workers-join.yml
   ```

5. **Start Deployment**  
   To start the deployment, run the following playbooks:
   ```bash
   ansible-playbook -i gcphosts ansible-start-deployment.yml
   ```

6. **Delete Deployment**  
   To delete the deployment, run the following playbooks:
   ```bash
   ansible-playbook -i gcphosts ansible-delete-deployment.yml
   ```

# Authors

João Maçãs
Rodrigo Ganância
Tiago Caixinha
