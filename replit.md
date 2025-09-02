# Overview

This is a personal portfolio website for Pema Tshering Sherpa, a Software Developer and Junior Data Scientist. The website is built as a Flask web application that serves a single-page portfolio with an interactive particle background effect. The design is inspired by https://p5aholic.me/ and features a dark theme with monospace typography. The portfolio includes sections for Home, About, Experience, Projects, and Contact, with a responsive design that works across desktop, tablet, and mobile devices.

# User Preferences

Preferred communication style: Simple, everyday language.

# System Architecture

## Frontend Architecture
The frontend is built as a single-page application using vanilla HTML, CSS, and JavaScript with the p5.js library for interactive graphics. The design follows a dark theme with monospace fonts and uses a fixed sidebar navigation for desktop and mobile-responsive layouts.

**Key Design Decisions:**
- **Single-page layout**: All content is contained in one HTML template for simplicity and smooth scrolling navigation
- **Interactive background**: Uses p5.js library to create particle/constellation effects that respond to user interaction
- **Responsive design**: CSS media queries and flexible layouts ensure compatibility across devices
- **Dark theme**: Black/dark grey background with light text for modern aesthetic and reduced eye strain

## Backend Architecture
The backend uses Flask, a lightweight Python web framework, following a minimal architecture suitable for a static portfolio site.

**Architecture Components:**
- **Flask application**: Simple server setup with a single route serving the portfolio template
- **Template engine**: Uses Flask's built-in Jinja2 templating to serve the HTML content
- **Environment configuration**: Uses environment variables for session secrets with fallback defaults
- **Static file serving**: Flask handles CSS, JavaScript, and asset delivery

**Rationale**: Flask was chosen for its simplicity since this is primarily a static portfolio site with minimal server-side logic required. The lightweight nature allows for easy deployment and maintenance.

## Data Storage
Currently no database is implemented as the portfolio content is static and embedded directly in the HTML template. All personal information, experience details, and project descriptions are hardcoded in the template.

**Future Considerations**: If dynamic content management is needed, a simple database could be added to store portfolio items, blog posts, or contact form submissions.

## Authentication & Security
- **Session management**: Flask session secret key configured via environment variables
- **No authentication required**: Portfolio is publicly accessible as intended for a personal showcase site

# External Dependencies

## Frontend Libraries
- **p5.js (v1.7.0)**: Creative coding library used for interactive particle background effects
- **Font Awesome (v6.4.0)**: Icon library for social media links and UI elements

## Backend Framework
- **Flask**: Python web framework for serving the application
- **Jinja2**: Template engine (included with Flask) for HTML templating

## Hosting & Deployment
- **Environment Variables**: Uses `SESSION_SECRET` for Flask session configuration
- **Port Configuration**: Configured to run on port 5000 with host binding to 0.0.0.0 for container compatibility

## Content Sources
- **Portfolio Content**: Based on requirements document for Pema Tshering Sherpa's personal information
- **Design Reference**: Visual design inspired by https://p5aholic.me/