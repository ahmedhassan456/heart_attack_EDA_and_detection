# Heart Attack EDA and Detection

This project provides a machine learning solution for heart attack detection using Flask and Docker. The system performs exploratory data analysis (EDA) and implements a prediction model for heart attack risk assessment.

## Prerequisites

### Installing Anaconda/Miniconda

1. Download Anaconda or Miniconda:
   - [Anaconda](https://www.anaconda.com/products/distribution)
   - [Miniconda](https://docs.conda.io/en/latest/miniconda.html)

2. Follow the installation instructions for your operating system:
   - Windows: Run the installer executable
   - Linux: `bash Anaconda-latest-Linux-x86_64.sh`
   - macOS: `bash Anaconda-latest-MacOSX-x86_64.sh`

3. Verify installation:
```bash
conda --version
```

### Installing Docker

1. Download Docker Desktop:
   - [Docker Desktop](https://www.docker.com/products/docker-desktop)

2. Installation by OS:
   - Windows: Run the Docker Desktop Installer
   - macOS: Drag Docker to Applications folder
   - Linux: Follow the [official guide](https://docs.docker.com/engine/install/)

3. Verify installation:
```bash
docker --version
```

## Project Setup

1. Clone the repository:
```bash
git clone https://github.com/ahmedhassan456/heart_attack_EDA_and_detection.git
cd heart_attack_EDA_and_detection
```

2. Create and activate Conda environment:
```bash
conda create -n heart_attack_env python=3.10.12
conda activate heart_attack_env
```

3. Install required packages:
```bash
pip install -r requirements.txt
```

## Local Development

1. Activate the Conda environment:
```bash
conda activate heart_attack_env
```

2. Run the Flask application:
```bash
python deployment/app.py
```

3. Access the application at `http://localhost:8000`

## Docker Deployment

1. Build the Docker image:
```bash
docker build -t heart-attack-detection .
```

2. Run the Docker container:
```bash
docker run -it -p 8000:8000 heart-attack-detection
```

3. Access the application at `http://127.0.0.1:8000`

## Project Structure

```
Heart Attack EDA and Detection/
├── deployment         # Folder contain the deployment files using Flask
    ├── controller          # Floder contain files to load and predict the model 
    ├── models/             # Trained model files
    ├── templates/          # HTML templates
    ├── app.py              # Flask application
├── test_model              # Folder contain the notebook and the data
├── Dockerfile         # Docker configuration
├── requirements.txt   # Python dependencies
└── README.md          # Project documentation
```

## API Endpoints

- `/`: Home page
- `/predict`: Endpoint for heart attack prediction

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.