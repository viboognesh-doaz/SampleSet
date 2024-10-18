# Step 1: Use the official Python base image
FROM python:3.9-slim

# Step 2: Set the working directory in the container
WORKDIR /app

# Step 3: Copy the requirements.txt file into the container
COPY requirements.txt .

# Step 4: Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Step 5: Copy the rest of the application code into the container
COPY . .

# Step 6: Expose the port that the Streamlit app will run on
EXPOSE 8501

# Step 7: Set the environment variable to avoid Streamlit asking for email
ENV STREAMLIT_BROWSER_GATHER_USAGE_STATS=False

# Step 8: Command to run the Streamlit app
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
