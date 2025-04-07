# Portfolio Website Deployment Guide

## Vercel Deployment with MySQL

### Prerequisites
- GitHub account
- Vercel account (free tier)
- MySQL database (PlanetScale or Railway recommended)

### Setup Instructions

1. **Set up MySQL Database**:
   - Create a free account on PlanetScale (planetscale.com) or Railway (railway.app)
   - Create a new MySQL database
   - Note down your database credentials (host, username, password, database name)

2. **Configure Environment Variables**:
   - In Vercel, go to your project settings
   - Add these environment variables:
     - MYSQL_HOST
     - MYSQL_USER  
     - MYSQL_PASSWORD
     - MYSQL_DATABASE

3. **Deploy to Vercel**:
   - Push this repository to GitHub
   - Connect your GitHub repo to Vercel
   - Vercel will automatically detect and deploy the Flask app

### Local Development
To run locally:
1. Create a `.env` file with your MySQL credentials
2. Install dependencies: `pip install -r requirements.txt`
3. Run: `python app.py`

### Notes
- The free tier has limitations on database connections
- Consider using connection pooling for production
