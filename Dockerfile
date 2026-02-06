# Dockerfile

# First stage: build the Streamlit app
FROM python:3.10-slim AS build

# Set working directory
WORKDIR /app

# Copy the requirements file
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Second stage: create a minimal production image
FROM python:3.10-slim AS production

# Set working directory
WORKDIR /app

# Copy the dependencies from the build stage
COPY --from=build /app .

# Expose the port Streamlit runs on
EXPOSE 8501

# Command to run the app
CMD ["streamlit", "run", "app.py"]