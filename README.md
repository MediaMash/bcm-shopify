# bcm-shopify Shopify App

## Overview

bcm-shopify is a Shopify app designed to pull videos from the BCM Admin https://github.com/MediaMash/mm-live-admin.

## Table of Contents

- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Installation

To install and use the bcm-shopify Shopify app, follow these steps:

1. **Clone the Repository**:
   ```shell
   git clone https://github.com/MediaMash/bcm-shopify.git
   cd bcm-shopify
   ```

2. **Set Up a Python Virtual Environment** (Optional but recommended):
   ```shell
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install Dependencies**:
   ```shell
   pip install -r requirements.txt
   ```

4. **Create a .env File**:
   Create a `.env` file in the project directory and set the necessary environment variables, including Shopify API keys and secrets. Example:
   ```
   SHOPIFY_API_KEY=your-api-key
   SHOPIFY_API_SECRET=your-api-secret
   SHOPIFY_REDIRECT_URI=your-app-redirect-uri
   DJANGO_API_BASE_URL=https://your-django-api-url.com
   ```

5. **Run the Application**:
   ```shell
   python app/app.py
   ```

6. **Access the App**:
   Visit `http://localhost:8000` in your web browser to access the app.

## Configuration

To configure bcm-shopify, you may need to make the following changes:

- **Shopify App Settings**: In your Shopify Partner account, configure the app's settings, including permissions, billing options (if applicable), and whitelisted redirection URLs.

- **OAuth2 Authentication**: Implement OAuth2 authentication in your app to securely connect to Shopify stores. Update the authentication settings accordingly.

- **Data Models**: Define data models in the `app/models` directory to match your app's data structure, e.g., `Video` and `Product`.

- **Routes and Controllers**: Customize routes and controllers in the `app/controllers` directory to handle specific actions and interactions.

- **Templates and Static Assets**: Modify HTML templates and static assets in the `app/templates` and `app/static` directories to customize your app's user interface.

## Usage

[Provide detailed instructions on how users can use your app within their Shopify store. Explain how to install the app on a store, how to access its features, and any configuration options.]

## Contributing

Contributions to bcm-shopify are welcome! If you have ideas, feature requests, or bug reports, please open an issue or submit a pull request.

## License

This project is licensed under the [License Name] - see the [LICENSE.md](LICENSE.md) file for details.
```

Replace the placeholder text with your specific app details and instructions. Additionally, make sure to include a license file (`LICENSE.md`) if applicable and provide any necessary attribution or licensing information for your code.
