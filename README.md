# Nairobi Urban Sprawl,Environmental and Impact Monitoring System

## 📍 Project Overview

This web-based GIS application visualizes and analyzes the impact of urban sprawl and deforestation in Nairobi from **2019 to 2023**. It provides spatial maps, statistical summaries, and downloadable datasets to help users understand urban expansion patterns and associated environmental changes.


## 💻 Features

- 🗺️ ** Map Images **: Visualizations of urban growth and forest loss from 2019 to 2023.
- 📊 **Summary Statistics**: Graphical and tabular representation of urban expansion and deforestation rates.
- 📥 **CSV Export**: Downloadable datasets for pollution, deforestation, and urban sprawl.
- 📄 **Help Page**: Provides guidance on using the system.
- ❌ **Custom 404 Page**: Enhanced user experience for invalid URLs.

---

## 🚀 Technologies Used

- **Backend**: Python, Django
- **Frontend**: HTML
- **GIS Tools**: Static map images 
- **Database**: SQLite (default Django database)



## 📂 Project Structure


sprawl/
├── gis_app/
│   ├── static/
│   │   ├── gis_app/
│   │   │   ├── map_data/           # Stores map images
│   │   │   └── css/                # Custom CSS files
│   ├── templates/
│   │   └── gis_app/
│   │       ├── base.html           # Base template
│   │       ├── index.html          # Homepage with maps and charts
│   │       ├── summary.html        # Summary statistics page
│   │       ├── help.html           # Help page
│   │       └── 404.html            # Custom error page
│   ├── urls.py                     # URL routing
│   ├── views.py                    # Django views
│   └── models.py                   # Django models
├── manage.py

