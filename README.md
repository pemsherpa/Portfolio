# Personal Portfolio Website

A modern, responsive personal portfolio website built with Flask, featuring an interactive particle background and clean design.

## Features

- **Interactive Background**: Dynamic particle system using p5.js
- **Responsive Design**: Works seamlessly on desktop, tablet, and mobile
- **Modern UI**: Dark theme with monospace typography
- **Smooth Navigation**: Single-page application with smooth scrolling
- **Professional Layout**: Clean, minimalist design showcasing your work

## Tech Stack

- **Backend**: Flask (Python web framework)
- **Frontend**: HTML5, CSS3, JavaScript
- **Graphics**: p5.js for interactive background
- **Icons**: Font Awesome
- **Styling**: Custom CSS with responsive design

## Prerequisites

- Python 3.8 or higher
- pip (Python package installer)

## Installation & Setup

### Step 1: Clone or Download the Project
```bash
# If using git
git clone <repository-url>
cd PortfolioPilot

# Or simply download and extract the project folder
```

### Step 2: Create a Virtual Environment (Recommended)
```bash
# On macOS/Linux
python3 -m venv venv
source venv/bin/activate

# On Windows
python -m venv venv
venv\Scripts\activate
```

### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 4: Run the Application
```bash
python app.py
```

### Step 5: Access the Website
Open your web browser and navigate to:
```
http://localhost:5000
```

## Project Structure

```
PortfolioPilot/
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
├── README.md             # This file
├── templates/            # HTML templates
│   ├── base.html        # Base template with navigation
│   ├── home.html        # Homepage content
│   ├── about.html       # About page content
│   ├── experience.html  # Experience page content
│   ├── projects.html    # Projects page content
│   └── contact.html     # Contact page content
└── attached_assets/      # Additional assets
```

## Customization

### Personal Information
Edit the HTML templates in the `templates/` folder to update:
- Your name and title
- About information
- Work experience
- Project details
- Contact information

### Styling
Modify the CSS in `templates/base.html` to customize:
- Colors and themes
- Typography
- Layout and spacing
- Responsive breakpoints

### Background Effects
Adjust the p5.js particle system in `templates/base.html`:
- Particle count and behavior
- Connection distances
- Mouse interaction sensitivity
- Animation speed

## Deployment

### Local Development
The app runs in debug mode by default for development. For production:

1. Set environment variable:
   ```bash
   export SESSION_SECRET="your-secure-secret-key"
   ```

2. Disable debug mode in `app.py`:
   ```python
   app.run(host='0.0.0.0', port=5000, debug=False)
   ```

### Production Deployment
For production deployment, consider using:
- **Gunicorn**: `gunicorn -w 4 -b 0.0.0.0:5000 app:app`
- **Docker**: Containerize the application
- **Cloud Platforms**: Deploy to Heroku, AWS, or similar services

## Troubleshooting

### Common Issues

1. **Port already in use**: Change the port in `app.py` or kill the process using port 5000
2. **Dependencies not found**: Ensure virtual environment is activated and run `pip install -r requirements.txt`
3. **Template errors**: Check that all HTML files are in the `templates/` folder

### Getting Help
If you encounter issues:
1. Check that all dependencies are installed correctly
2. Verify Python version compatibility
3. Ensure all template files are present
4. Check console output for error messages

## License

This project is open source and available under the MIT License.
