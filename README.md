# Ollama Local API Serving

A Docker-based FastAPI wrapper for Ollama that enables easy local deployment and API access to Large Language Models (LLMs). This repository provides a complete solution for running Ollama models locally with a REST API interface, perfect for development, testing, and integration purposes.

## 🎯 Purpose

This repository serves as a comprehensive guide and ready-to-use setup for:

- **Local LLM Deployment**: Run open-source language models locally using Ollama
- **API Integration**: Provide a REST API interface for easy integration with applications
- **Development & Testing**: Ideal environment for testing LLM capabilities and building AI-powered applications
- **Privacy-First AI**: Keep your data local while leveraging powerful language models

## ✨ Features

- 🐳 **Dockerized Setup**: Complete containerization with Docker Compose
- 🚀 **FastAPI Wrapper**: Modern, fast API framework with automatic documentation
- 🔄 **Health Monitoring**: Built-in health checks and status endpoints
- 📋 **Model Management**: Easy model listing and management
- 🌐 **Network Isolation**: Secure internal networking between services
- 🔧 **Environment Configuration**: Flexible configuration via environment variables

## 🛠 Prerequisites

Before getting started, ensure you have the following installed:

- **Docker**: [Install Docker](https://docs.docker.com/get-docker/)
- **Docker Compose**: Usually included with Docker Desktop
- **Python 3.11+**: For local development (optional)

## 📁 Repository Structure

```
Ollama_Local_API_Serving/
├── docker-compose.yml      # Docker Compose configuration
├── Dockerfile             # FastAPI service container definition
├── main.py               # FastAPI application with API endpoints
├── requirements.txt      # Python dependencies
└── README.md            # This file
```

## 🚀 Quick Start

### 1. Clone the Repository

```bash
git clone https://github.com/Ahmetyasin/Ollama_Local_API_Serving.git
cd Ollama_Local_API_Serving
```

### 2. Configure Model Storage (Important)

Update the volume path in `docker-compose.yml` to match your system:

```yaml
volumes:
  - /path/to/your/models:/root/.ollama/models  # Update this path
```

**For macOS users**: Replace `/Users/ahmetyasinaytar/Desktop/models` with your preferred model storage location.

### 3. Start the Services

```bash
docker compose up -d
```

This will:
- Pull the latest Ollama image
- Build the FastAPI wrapper
- Start both services with proper networking
- Expose Ollama on port `11434` and FastAPI on port `8000`

### 4. Pull Your First Model

```bash
# Pull a model (e.g., Llama 2)
docker exec ollama-api-server ollama pull llama2

# Or any other model you prefer
docker exec ollama-api-server ollama pull codellama
```

## 📚 API Documentation

Once running, access the interactive API documentation:

- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

### Available Endpoints

#### Health Check
```http
GET /health
```
Returns the service status and Ollama connection information.

#### List Available Models
```http
GET /models
```
Returns all locally available Ollama models.

#### Generate Text
```http
POST /generate
```

**Request Body:**
```json
{
  "model": "llama2",
  "prompt": "Explain quantum computing in simple terms",
  "stream": false
}
```

**Response:**
```json
{
  "model": "llama2",
  "created_at": "2024-01-15T10:30:00Z",
  "response": "Quantum computing is...",
  "done": true
}
```

## 💻 Usage Examples

### Using cURL

```bash
# Check health
curl http://localhost:8000/health

# List models
curl http://localhost:8000/models

# Generate text
curl -X POST http://localhost:8000/generate \
  -H "Content-Type: application/json" \
  -d '{
    "model": "llama2",
    "prompt": "Write a Python function to calculate fibonacci numbers",
    "stream": false
  }'
```

### Using Python Requests

```python
import requests

# Generate text
response = requests.post(
    "http://localhost:8000/generate",
    json={
        "model": "llama2",
        "prompt": "What are the benefits of containerization?",
        "stream": False
    }
)

result = response.json()
print(result["response"])
```

## 🔧 Configuration

### Environment Variables

The FastAPI service supports the following environment variables:

| Variable | Default | Description |
|----------|---------|-------------|
| `OLLAMA_HOST` | `ollama` | Hostname of the Ollama service |
| `OLLAMA_PORT` | `11434` | Port of the Ollama service |

### Custom Configuration

To modify the configuration, update the `environment` section in `docker-compose.yml`:

```yaml
environment:
  - OLLAMA_HOST=ollama
  - OLLAMA_PORT=11434
```

## 🖥 Tested Environment

This setup has been successfully tested on:

- **Hardware**: Mac M3 Pro (ARM64 architecture)
- **OS**: macOS (Apple Silicon)
- **Docker**: Docker Desktop for Mac

> **Note**: This configuration works seamlessly on Apple Silicon Macs and should work on other platforms with minimal adjustments.

## 🐛 Troubleshooting

### Common Issues

1. **Port Already in Use**
   ```bash
   # Check what's using the port
   lsof -i :8000
   lsof -i :11434
   ```

2. **Model Storage Issues**
   - Ensure the volume path in `docker-compose.yml` exists and is writable
   - Check Docker has permission to access the directory

3. **Service Not Starting**
   ```bash
   # Check service logs
   docker compose logs ollama
   docker compose logs fastapi-wrapper
   ```

4. **Model Not Found**
   ```bash
   # List available models
   docker exec ollama-api-server ollama list
   
   # Pull missing model
   docker exec ollama-api-server ollama pull <model-name>
   ```

### Performance Tips

- **Memory**: Ensure sufficient RAM for your chosen models (8GB+ recommended)
- **Storage**: Models can be large (2-7GB each), ensure adequate disk space
- **CPU**: While GPU acceleration isn't required, more CPU cores improve performance

## 🔄 Alternative Running Methods

### Option 1: Docker Compose (Recommended)
```bash
docker compose up -d
```

### Option 2: Local Development
```bash
# Install dependencies
pip install -r requirements.txt

# Start Ollama separately
docker run -d -p 11434:11434 ollama/ollama

# Start FastAPI
uvicorn main:app --host 0.0.0.0 --port 8000
```

## 🤝 Contributing

Contributions are welcome! Please feel free to submit issues, feature requests, or pull requests.

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request


## 🙏 Acknowledgments

- [Ollama](https://ollama.ai/) for providing an excellent local LLM platform
- [FastAPI](https://fastapi.tiangolo.com/) for the modern API framework
- The open-source community for continuous inspiration and support

## 📞 Support

If you encounter any issues or have questions:

1. Check the [troubleshooting section](#-troubleshooting)
2. Search existing [issues](https://github.com/Ahmetyasin/Ollama_Local_API_Serving/issues)
3. Create a new issue with detailed information

---

**Happy coding!** 🚀 This setup provides a solid foundation for local AI development and testing. Whether you're building chatbots, content generators, or experimenting with LLMs, this API wrapper makes integration seamless and straightforward.
