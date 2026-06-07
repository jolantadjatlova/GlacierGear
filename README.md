# [GlacierGear](https://glaciergear-7ce99fc7bac4.herokuapp.com/)
 
Developer: Jolanta Djatlova ([jolantadjatlova](https://github.com/jolantadjatlova))
 
GlacierGear is a full-stack e-commerce web application that allows users to browse, search, and filter ski and snowboard rental equipment. Registered users can add items to a booking cart, select rental dates, and complete a secure payment via Stripe. Store owners can manage products directly through the frontend.
 
The application focuses on clean UX design, accessibility, and secure authentication, providing a complete rental booking solution for a ski equipment shop based in Borlänge, Sweden.
 
![screenshot](docs/am_i_responsive.png)
 
 
### Contents
 
- [UX](#ux)
  - [The 5 Planes of UX](#the-5-planes-of-ux)
    - [1. Strategy](#1-strategy)
    - [2. Scope](#2-scope)
    - [3. Structure](#3-structure)
    - [4. Skeleton](#4-skeleton)
    - [5. Surface](#5-surface)
  - [User Goals](#user-goals)
  - [User Stories](#user-stories)
- [Design Choices](#design-choices)
  - [Wireframes](#wireframes)
  - [Typography](#typography)
  - [Colour Scheme](#colour-scheme)
  - [Images](#images)
  - [Responsiveness](#responsiveness)
- [Agile Development Process](#agile-development-process)
  - [Planning Tools & Workflow](#planning-tools--workflow)
    - [GitHub Projects (Kanban)](#github-projects-kanban)
    - [GitHub Issues](#github-issues)
    - [MoSCoW Prioritization](#moscow-prioritization)
- [Features](#features)
  - [Existing Features](#existing-features)
  - [Future Enhancements](#future-enhancements)
- [Data Model & Relationships](#data-model--relationships)
  - [Entity Relationship Diagram](#entity-relationship-diagram)
  - [Database Models](#database-models)
  - [Database Relationships Summary](#database-relationships-summary)
  - [Database Implementation](#database-implementation)
- [CRUD Functionality](#crud-functionality)
- [Security Features](#security-features)
- [Technologies Used](#technologies-used)
- [Testing](#testing)
  - [Automated Testing](#automated-testing)
  - [Bugs](#bugs)
  - [Responsiveness Test](#responsiveness-test)
  - [Code Validation](#code-validation)
    - [HTML](#html)
    - [CSS](#css)
    - [JavaScript](#javascript)
    - [Python](#python-pep8)
  - [User Story Testing](#user-story-testing)
  - [Feature Testing](#feature-testing)
  - [Accessibility Testing](#accessibility-testing)
  - [Lighthouse Testing](#lighthouse-testing)
  - [Browser Testing](#browser-testing)
- [Deployment](#deployment)
  - [Heroku Deployment](#heroku-deployment)
  - [AWS S3](#aws-s3)
  - [PostgreSQL Database](#postgresql-database)
  - [Stripe Payments](#stripe-payments)
  - [Local Development](#local-development)
    - [To Clone the Project](#to-clone-the-project)
  - [To Fork the Project](#to-fork-the-project)
- [Credits](#credits)
  - [Feedback, Advice and Support](#feedback-advice-and-support)
  - [Learning Help and Resources](#learning-help-and-resources)
  - [Images](#images-1)

## UX
### The 5 Planes of UX
#### 1. Strategy
##### Purpose
- Provide a simple and intuitive platform for users to browse and rent ski and snowboard equipment online.
- Allow users to select rental dates, choose sizes, and complete a secure payment through Stripe.
- Enable store owners to manage products directly through the frontend without accessing the Django admin panel.
- Offer a visually appealing and easy-to-use interface that supports a seamless booking experience across all devices.
##### Primary User Needs
- Easily browse and view rental products without needing to create an account.
- Quickly search and filter products by category, size, gender, colour, and garment type.
- Add items to a booking cart and complete a rental booking securely.
- Create an account to view booking history and save default contact information.
- Access the website seamlessly across mobile, tablet, and desktop devices.
##### Project Goals
- Build a full-stack Django e-commerce application demonstrating CRUD functionality and Stripe payment integration.
- Implement user authentication to support personalised features such as booking history and saved profile information.
- Apply UX best practices, including intuitive navigation, responsive design, and clear user feedback.
- Use consistent styling and clear typography to support readability and usability.
#### 2. Scope
 
##### Functional Requirements
- Users can browse all products without needing to create an account.
- Users can view full product details including size availability and pricing.
- Users can search for products using keywords.
- Users can filter products by category, size, gender, colour, and garment type.
- Users can register for an account and log in securely.
- Authenticated users can add products to a booking cart with selected rental dates.
- Authenticated users can adjust quantities and remove items from their cart.
- Authenticated users can complete a secure checkout using Stripe.
- Authenticated users can view their booking history on their profile page.
- Authenticated users can save their default phone number to their profile.
- Superusers can add, edit, and delete products through the frontend.
- The website provides clear feedback messages when actions are completed.
##### Content Requirements
- Product names, images, descriptions, prices, sizes, and stock levels.
- Category-based product organisation.
- Clear navigation labels and page headings.
- Form labels and validation messages to guide user input.
- Accessible text and colour contrast for readability.
#### 3. Structure
 
##### Interaction Design
The website follows a clear and intuitive user flow focused on product discovery and rental booking. Public users can browse, search, and filter products, while authenticated users can access the booking cart, checkout, and profile features. Clear UI feedback is provided throughout user interactions via toast notifications.
 
##### Information Architecture
Content is organised into clear sections including the homepage with live weather widget, product listings with filtering and sorting, product detail pages with size and date selection, a booking cart, checkout, and user profile with booking history. Categories are used to group products and support easy navigation.
 
##### Navigation Layout
A persistent navigation bar provides access to key areas of the site, including Home, Ski Outfits, Snowboard Outfits, Accessories, My Bookings, and user account options. The navigation collapses into a mobile-friendly menu on smaller screens.
 
##### User Flow
Users arrive on the homepage and can immediately browse products or use the search. Authenticated users can add items to their cart, select rental dates, and complete a booking through the secure Stripe checkout. After checkout, users receive a confirmation email and can view their booking history on their profile page.
 
 
#### 4. Skeleton
 
Wireframes were used to plan page layout, navigation placement, and content hierarchy before visual styling was applied. Key interface elements such as the navigation bar, search functionality, product cards, booking cart, and checkout form were positioned to ensure clarity and ease of use across different screen sizes.
 
The wireframes created can be viewed in the [Wireframes](#wireframes) section.
 
 
#### 5. Surface
 
The surface design of *GlacierGear* focuses on creating a clean, modern, and alpine-inspired visual experience. A navy and white colour scheme with mountain imagery conveys trust and the outdoor ski theme. The interface prioritises clarity and readability, ensuring users can easily focus on browsing and booking equipment.
 
Further visual decisions are detailed in the [Typography](#typography) and [Colour Scheme](#colour-scheme) sections.
 
 
[Back to contents](#contents)
 
---

### User Goals
 
#### Public Users
- To browse and view rental products without needing to create an account.
- To search and filter products to quickly find suitable equipment.
#### Authenticated Users
- To create an account and log in securely to access booking features.
- To add products to a booking cart and complete a secure rental booking.
- To view booking history and manage saved profile information.
- To receive clear confirmation of bookings via email and on-screen notifications.
#### Store Owners (Superusers)
- To add, edit, and delete products through the frontend product management interface.
### User Stories
 
#### Public Users
- As a public user, I want to browse all products so that I can see what equipment is available to rent.
- As a public user, I want to filter products by category, size, and colour so that I can quickly find equipment that suits me.
- As a public user, I want to search for products by keyword so that I can locate specific items quickly.
- As a public user, I want to view product details including sizes and pricing so that I can make an informed decision.
#### Authenticated Users
- As an authenticated user, I want to create an account so that I can make bookings and view my booking history.
- As an authenticated user, I want to add products to a booking cart and select rental dates so that I can plan my rental.
- As an authenticated user, I want to complete a secure checkout using my card so that I can confirm my booking.
- As an authenticated user, I want to receive a booking confirmation email so that I have a record of my rental.
- As an authenticated user, I want to view my booking history on my profile page so that I can track past rentals.
#### Store Owners
- As a store owner, I want to add new products to the store so that customers can see the latest equipment.
- As a store owner, I want to edit existing products so that I can update pricing, descriptions, and images.
- As a store owner, I want to delete products so that I can remove discontinued equipment from the store.
[Back to contents](#contents)
 
---
## Design Choices
 
### Wireframes
 
These wireframes were created using [Balsamiq](https://balsamiq.com/) during the Scope Plane part of the design and planning process for this project.
 
- [Home Page](docs/wireframe_home.png)
- [Products Page](docs/wireframe_products.png)
- [Product Detail Page](docs/wireframe_product_detail.png)
- [Booking Cart](docs/wireframe_bag.png)
- [Checkout Page](docs/wireframe_checkout.png)
- [Profile Page](docs/wireframe_profile.png)
- [Sign In](docs/wireframe_login.png)
- [Sign Up](docs/wireframe_signup.png)
- [404 Page](docs/wireframe_404.png)
### Typography
 
- The **Bebas Neue** typeface is used for headings and hero text to create a bold, sporty aesthetic that reflects the ski and snowboard theme of the project.
- **Open Sans** (via system fonts / Bootstrap defaults) is used for body text and navigation due to its clean, readable letterforms across different screen sizes.
- Varying font weights are used to establish clear visual hierarchy between headings, navigation elements, and content text.
- This typography pairing supports a modern and active interface while keeping the layout clear and easy to navigate.
### Colour Scheme
 
The colour palette was designed to reflect the alpine ski theme of GlacierGear. Navy blue and white form the core palette, evoking snow, sky, and mountain environments. Accent colours are used to highlight interactive elements while keeping the interface clean and professional.
 
**Primary colours:**
- Navy Dark: `#1a2744`
- Navy: `#2d3f6b`
- White: `#ffffff`
![GlacierGear Colour Palette](docs/glaciergear_palette.png)
 
 
### Images
 
The hero background image and card images used on the GlacierGear homepage were sourced from free stock photography sites and optimised for web use. Product images were sourced from free stock photography and uploaded through the Django admin panel.
 
All images include descriptive `alt` attributes to support accessibility.

### Responsiveness
 
The GlacierGear application is fully responsive and adapts to different screen sizes using **Bootstrap's responsive grid system**.
 
The layout, typography, and interactive elements adjust to maintain usability across mobile, tablet, and desktop devices.
 
- Navigation collapses into a mobile-friendly menu on smaller screens.
- Product cards reflow from a 4-column to 2-column to 1-column grid on smaller screens.
- Forms, buttons, and inputs remain accessible and easy to use on touch devices.
Responsiveness was tested using browser developer tools and manual viewport resizing.
Further details can be found in the **Responsiveness Test** section.
 
 
[Back to contents](#contents)

## Agile Development Process
 
GlacierGear was developed using an iterative Agile approach, focusing on delivering a clear and user-friendly Minimum Viable Product (MVP). Development was carried out in small, manageable stages, allowing functionality to be built, tested, and refined incrementally.
 
The workflow was managed using GitHub Projects (Kanban board) and GitHub Issues, where user stories and tasks were prioritised using the MoSCoW method. This ensured that core functionality such as product browsing, the booking cart, Stripe checkout, and user profiles was implemented first, followed by usability and design improvements.
 
[Back to contents](#contents)
 
---
 
### Planning Tools & Workflow
 
#### GitHub Projects (Kanban)
A Kanban board was created using [GitHub Projects](https://github.com/jolantadjatlova/GlacierGear/projects) to visually manage tasks and track progress. Tasks were broken down into user stories and categorised by status:
 
- To Do
- In Progress
- Done
![GitHub Projects Board](docs/glaciergear_project_board.png)
 
#### GitHub Issues
 
GitHub Issues were used to record user stories, development tasks and potential features, with labels applied.
 
![GitHub Issues](docs/glaciergear_github_issues.png)
 
#### MoSCoW Prioritization
 
The MoSCoW prioritisation method was used to classify tasks as Must Have, Should Have or Could Have. This helped ensure that essential functionality was delivered within the project timeframe.
 
 
[Back to contents](#contents)
 
---
## Features
 
### Existing Features
 
#### Navbar
 
A single, responsive navigation bar is used across the entire site to provide consistent access to key areas of the application.
 
The navbar displays the GlacierGear logo on the left, navigation links in the centre, and account/cart icons on the right. Navigation options update dynamically based on authentication status. Superusers see a Product Management link in their account dropdown.
 
![Desktop navbar](docs/navbar_desktop.png)
 
![Mobile navbar](docs/navbar_mobile.png)
 
---
 
#### Home Page
 
The home page acts as a welcoming entry point with a full-width hero image, a live weather widget showing current conditions in Borlänge, and three product category cards.
 
The page includes:
- A live weather widget (temperature, description) powered by Open-Meteo API
- A hero heading and call-to-action button
- Category cards for Ski Outfits, Snowboard Outfits, and How It Works
- A pickup location section with an interactive Leaflet map
![Home page](docs/home_desktop.png)
 
---
 
#### Live Weather Widget
 
The homepage displays live weather data for Borlänge, Sweden, fetched from the [Open-Meteo API](https://open-meteo.com/) on each page load. No API key is required.
 
The widget shows:
- Current temperature in °C
- Weather description (e.g. Mainly Clear, Light Snow)
If the API is unavailable, the widget gracefully shows "Weather unavailable" without breaking the page.
 
![Weather widget](docs/weather_widget.png)
 
---
 
#### Product Listing Page
 
Users can browse all available rental products with filtering and sorting options.
 
Features include:
- Filter by gender, garment type, size, and colour
- Sort by price, name, and rating
- Product count displayed
- Edit/Delete links visible to superusers on each card
![Products page](docs/products_desktop.png)
 
---
 
#### Product Detail Page
 
Each product has a dedicated detail page showing full information and a booking form.
 
Features include:
- Product image, name, description, badges, and price per day
- Size selection with sold out indicators and low stock warnings (≤2 remaining)
- Rental date picker (start and end date)
- Quantity selector
- Superuser edit/delete buttons
![Product detail page](docs/product_detail_desktop.png)
 
---
 
#### Booking Cart
 
Users can review their selected items before checkout.
 
Features include:
- Product image, name, size, dates, quantity, and line total
- Rental days summary
- Update quantity and remove item options
- Cart total and checkout button
![Booking cart](docs/bag_desktop.png)
 
---
 
#### Checkout
 
Users complete their booking through a secure Stripe-powered checkout.
 
Features include:
- Booking details form (name, email, phone, rental dates)
- Pre-filled with saved profile information
- Save info checkbox to update profile on checkout
- Stripe card payment element
- Loading overlay during payment processing
![Checkout page](docs/checkout_desktop.png)
 
---
 
#### Checkout Success / Booking Confirmation
 
After a successful payment, users see a booking confirmation page.
 
Features include:
- Booking reference number
- Customer details and rental dates
- Line items with sizes and totals
- Pickup location and opening hours
- Back to Profile button (if coming from booking history)
A confirmation email is also sent automatically via Stripe webhooks.
 
![Checkout success](docs/checkout_success_desktop.png)
 
---
 
#### User Profile
 
Authenticated users have a profile page showing their account details, contact information, and full booking history.
 
Features include:
- Email and username display
- Phone number update form
- Booking history table with links to past confirmations
![Profile page](docs/profile_desktop.png)
 
---
 
#### Product Management (Superusers)
 
Superusers can add, edit, and delete products directly through the frontend.
 
Features include:
- Add Product page accessible from the account dropdown
- Edit Product page pre-filled with existing product data
- Delete confirmation on product cards and detail pages
- Superuser-only buttons visible on product cards and detail pages
![Add product page](docs/add_product_desktop.png)
 
---
 
#### Allauth Authentication Pages
 
All authentication pages (login, signup, logout, password reset etc.) are fully styled to match the GlacierGear design with the navy card layout.
 
![Login page](docs/login_desktop.png)
 
---
 
#### Toast Notifications
 
Real-time feedback is provided via Bootstrap toast notifications for all key actions.
 
Success toasts show bag contents (except on the profile page). Error, warning, and info toasts are also displayed where appropriate.
 
![Toast notification](docs/toast_success.png)
 
---
 
#### 404 and 500 Error Pages
 
Custom error pages are implemented to maintain visual consistency when errors occur.
 
![404 page](docs/404_desktop.png)
 
---
 
### Future Enhancements
 
- **Wishlist** — Allow users to save products to a wishlist for future reference.
- **Product Reviews** — Allow authenticated users to leave reviews and ratings on products they have rented.
- **Email notifications for low stock** — Automatically notify the store owner when a product size reaches zero stock.
- **Discount codes** — Allow store owners to create promotional discount codes for checkout.
[Back to contents](#contents)
 
---
## Data Model & Relationships
 
The GlacierGear application uses a relational database structure. The main models are: User, UserProfile, Category, Product, ProductSize, Booking, and BookingLineItem.
 
### Entity Relationship Diagram
 
![Entity Relationship Diagram](docs/entity_relationship_diagram.png)
 
### Database Models
 
#### User (Django Authentication)
The User model is provided by Django's built-in authentication system.
 
**Fields:**
- `id`: AutoField (Primary Key)
- `username`: CharField — Unique username
- `email`: EmailField — User's email address
- `password`: CharField — Hashed password
---
 
#### UserProfile
Stores default contact information and links to booking history.
 
**Fields:**
- `user`: OneToOneField(User) — Links to Django User
- `default_phone_number`: CharField — Optional saved phone number
---
 
#### Category
Organises products into rental categories.
 
**Fields:**
- `id`: AutoField (Primary Key)
- `name`: CharField — Internal category name (e.g. `ski_outfit`)
- `friendly_name`: CharField — Display name (e.g. `Ski Outfit`)
---
 
#### Product
Stores all rental product information.
 
**Fields:**
- `category`: ForeignKey(Category)
- `name`: CharField
- `description`: TextField
- `price_per_day`: DecimalField — Rental price per day in SEK
- `image`: ImageField
- `has_sizes`: BooleanField — Whether the product has size variants
- `sport`: CharField — e.g. ski, snowboard
- `garment_type`: CharField — e.g. jacket, trousers, full_set
- `color`: CharField
- `rating`: DecimalField
---
 
#### ProductSize
Tracks size availability and stock for each product.
 
**Fields:**
- `product`: ForeignKey(Product)
- `size`: CharField — e.g. XS, S, M, L, XL
- `stock`: IntegerField — Number of units available
---
 
#### Booking
Stores completed rental booking information.
 
**Fields:**
- `booking_number`: CharField — Unique auto-generated reference
- `user_profile`: ForeignKey(UserProfile) — Links to user
- `full_name`: CharField
- `email`: EmailField
- `phone_number`: CharField
- `rental_start_date`: DateField
- `rental_end_date`: DateField
- `rental_days`: IntegerField
- `date`: DateTimeField — When the booking was placed
- `grand_total`: DecimalField
- `original_bag`: TextField — JSON snapshot of the bag
- `stripe_pid`: CharField — Stripe payment intent ID
---
 
#### BookingLineItem
Stores individual items within a booking.
 
**Fields:**
- `booking`: ForeignKey(Booking)
- `product`: ForeignKey(Product)
- `size`: CharField
- `quantity`: IntegerField
- `lineitem_total`: DecimalField
---
 
### Database Relationships Summary
 
1. **User → UserProfile (1:1)** — Auto-created on registration via signal
2. **UserProfile → Booking (1:N)** — One profile can have many bookings
3. **Category → Product (1:N)** — One category contains many products
4. **Product → ProductSize (1:N)** — One product has many size variants
5. **Booking → BookingLineItem (1:N)** — One booking contains many line items
6. **Product → BookingLineItem (1:N)** — One product can appear in many line items
### Database Implementation
 
**Production Database:** PostgreSQL (Neon), connected via `DATABASE_URL` environment variable.
 
**Local Development Database:** SQLite3 (Django default).
 
 
[Back to contents](#contents)
 
---
## CRUD Functionality
 
| Operation | Feature | Access | Description |
|-----------|---------|--------|-------------|
| **Create** | Add Product | Superuser | Add new rental products with images via frontend form |
| **Create** | Make Booking | Authenticated | Create a booking via cart and Stripe checkout |
| **Read** | Browse Products | Public | View all products with filtering and sorting |
| **Read** | Product Detail | Public | View full product details, sizes, and stock |
| **Read** | Booking History | Authenticated | View past bookings on profile page |
| **Update** | Edit Product | Superuser | Update product details, pricing, and images |
| **Update** | Update Profile | Authenticated | Save default phone number to profile |
| **Update** | Update Cart | Authenticated | Adjust quantities in booking cart |
| **Delete** | Delete Product | Superuser | Remove products from the store |
| **Delete** | Remove Cart Item | Authenticated | Remove items from the booking cart |
 
 
[Back to contents](#contents)
 
---
## Security Features
 
### Authentication & Authorisation
- User authentication is implemented using **Django Allauth**.
- Only authenticated users can access the booking cart, checkout, and profile pages.
- Superuser checks are applied at view level for all product management views.
### Access Control
- Django's `@login_required` decorator is used to protect all private views.
- Superuser access is verified using `request.user.is_superuser` in views.
- Unauthorised access attempts redirect users to the home page with an error message.
### Payment Security
- Payments are processed entirely through **Stripe** — no card data touches the GlacierGear server.
- Stripe webhooks verify payment completion independently of the checkout view.
- A 5-attempt webhook retry loop ensures orders are created even if the checkout view fails.
### Form Validation
- Django ModelForms validate all user input.
- Rental date validation ensures end date is after start date.
- Stock checks prevent adding out-of-stock items to the cart.
### CSRF Protection
- Django's built-in CSRF protection is enabled on all forms.
### Environment Variables
- Sensitive data (SECRET_KEY, Stripe keys, AWS credentials, database URL) are stored in environment variables.
- No sensitive information is committed to the repository.
- `DEBUG` mode is disabled in production.
[Back to contents](#contents)
 
---
## Technologies Used
 
| Technology | Purpose | Type |
|-------------|----------|------|
| [Git](https://git-scm.com/) | Version control throughout development | Tool |
| [GitHub](https://github.com/) | Store the project repository | Tool |
| [VS Code](https://code.visualstudio.com/) | Write and edit all project code | Tool |
| [HTML](https://developer.mozilla.org/en-US/docs/Web/HTML) | Structure page content and templates | Language |
| [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS) | Style the user interface | Language |
| [JavaScript](https://developer.mozilla.org/en-US/docs/Web/JavaScript) | Frontend interactivity (Stripe, date picker, filters) | Language |
| [Python](https://www.python.org/) | Backend logic, views, and data handling | Language |
| [Django](https://www.djangoproject.com/) | Full-stack web framework | Framework |
| [Django Allauth](https://django-allauth.readthedocs.io/) | User authentication and account management | Library |
| [Bootstrap 5](https://getbootstrap.com/) | Responsive layout and UI components | Library |
| [Bootstrap Icons](https://icons.getbootstrap.com/) | Icons throughout the interface | Library |
| [Django Crispy Forms](https://django-crispy-forms.readthedocs.io/) | Form rendering with Bootstrap styling | Library |
| [Stripe](https://stripe.com/) | Secure payment processing and webhooks | Service |
| [Open-Meteo API](https://open-meteo.com/) | Live weather data for Borlänge homepage widget | API |
| [Leaflet.js](https://leafletjs.com/) | Interactive map on homepage pickup location | Library |
| [PostgreSQL](https://www.postgresql.org/) | Production database | Database |
| [SQLite3](https://www.sqlite.org/) | Local development database | Database |
| [Amazon S3](https://aws.amazon.com/s3/) | Static and media file storage in production | Cloud Service |
| [Heroku](https://www.heroku.com/) | Deploy and host the live application | Platform |
| [Neon](https://neon.tech/) | Managed PostgreSQL database provider | Service |
| [Balsamiq](https://balsamiq.com/) | Wireframes for planning layout and user flow | Tool |
| [Coolors](https://coolors.co/) | Colour palette generation | Tool |
| [W3C HTML Validator](https://validator.w3.org/) | Validate HTML structure | Tool |
| [W3C CSS Validator](https://jigsaw.w3.org/css-validator/) | Validate CSS syntax | Tool |
| [Lighthouse](https://developer.chrome.com/docs/lighthouse/) | Performance and accessibility testing | Tool |
| [WAVE](https://wave.webaim.org/) | Accessibility evaluation | Tool |
| [ChatGPT](https://chat.openai.com/) | Content writing assistance and code guidance | AI |
 
 
[Back to contents](#contents)
 
---
## Testing
 
### Automated Testing
 
Automated testing was implemented using Django's built-in testing framework.
 
Tests were written for:
- Models (data integrity and field validation)
- Forms (validation of required fields and date logic)
- Views (page loading, authentication, permissions)
All tests were run using:
 
`python manage.py test --verbosity=2`
 
![Automated tests passing](docs/automated_tests.png)
 
 
### Bugs
 
| **Bug** | **Status** | **Description** | **Steps to Resolve** |
|--------|------------|-----------------|----------------------|
| `lineitem_total` DecimalField overflow | Fixed | The `max_digits=6` caused errors for large rentals. | Increased `max_digits` to 10 on the `BookingLineItem` model. |
| Checkout form not pre-filling dates | Fixed | Session rental dates were not passed to the checkout form. | Added `rental_start_date` and `rental_end_date` from session to the form initial data. |
| Stripe webhook creating duplicate orders | Fixed | Orders were being created twice when both the view and webhook ran. | Added `original_bag` and `stripe_pid` fields to `Booking` and matched on these in the webhook handler. |
| Stock not decrementing on webhook-created orders | Fixed | If the checkout view failed and the webhook created the order, stock was not decremented. | Added `_decrement_stock()` method to the webhook handler called only when it creates the order. |
| Static files not loading on Heroku | Fixed | After removing `DISABLE_COLLECTSTATIC`, the build failed due to missing `STATIC_ROOT`. | Added `STATIC_ROOT` to both the `USE_AWS` and non-AWS settings blocks. |
| Allauth pages not styled | Fixed | Logout, password reset, and other allauth pages used default unstyled templates. | Created custom styled templates for all allauth account pages extending `base.html`. |
| Weather widget showing hardcoded values | Fixed | The homepage weather pill displayed `-2°C Partly Cloudy` regardless of the API. | Updated `index.html` to use `{{ weather.temperature }}` and `{{ weather.description }}` from context. |
| Hero background image not covering cards on mobile | Fixed | The background image was set on `body`, staying fixed to the viewport. On mobile, stacked cards pushed below the visible image area. | Moved the background image from `body` to `.hero` so it scales naturally with the hero section as cards stack vertically. |
| Confirmation email not sending after checkout | Fixed | The `checkout_success` view wasn't calling `send_mail` after a successful booking, so no confirmation email was sent to the user. | Added `send_mail` call directly to the `checkout_success` view using the existing email templates. |
| Stripe webhook returning 500 error | Fixed | `stripe.Charge.retrieve` was incompatible with the newer Stripe API version, causing the webhook handler to crash on every payment. | Updated webhook handler to use `intent.charges.data[0].billing_details` and `intent.amount_received` instead. |
 
[Back to contents](#contents)
 
---
 
### Responsiveness Test
 
| **Page** | **Mobile** | **Tablet** | **Desktop** | **Notes** |
|-----------|------------|------------|-------------|-----------|
| **Home** | ![](docs/home_mobile.png) | ![](docs/home_tablet.png) | ![](docs/home_desktop.png) | Works as expected |
| **Products** | ![](docs/products_mobile.png) | ![](docs/products_tablet.png) | ![](docs/products_desktop.png) | Works as expected |
| **Product Detail** | ![](docs/product_detail_mobile.png) | ![](docs/product_detail_tablet.png) | ![](docs/product_detail_desktop.png) | Works as expected |
| **Booking Cart** | ![](docs/bag_mobile.png) | ![](docs/bag_tablet.png) | ![](docs/bag_desktop.png) | Works as expected |
| **Checkout** | ![](docs/checkout_mobile.png) | ![](docs/checkout_tablet.png) | ![](docs/checkout_desktop.png) | Works as expected |
| **Checkout Success** | ![](docs/checkout_success_mobile.png) | ![](docs/checkout_success_tablet.png) | ![](docs/checkout_success_desktop.png) | Works as expected |
| **Profile** | ![](docs/profile_mobile.png) | ![](docs/profile_tablet.png) | ![](docs/profile_desktop.png) | Works as expected |
| **Login** | ![](docs/login_mobile.png) | ![](docs/login_tablet.png) | ![](docs/login_desktop.png) | Works as expected |
| **Sign Up** | ![](docs/signup_mobile.png) | ![](docs/signup_tablet.png) | ![](docs/signup_desktop.png) | Works as expected |
| **Add Product** | ![](docs/add_product_mobile.png) | ![](docs/add_product_tablet.png) | ![](docs/add_product_desktop.png) | Works as expected |
 
 
[Back to contents](#contents)
 
---
 
### Code Validation
 
#### HTML
 
All major templates were tested using the [W3C HTML Validator](https://validator.w3.org/).
 
| Page | Result |
|------|--------|
| Home | ![](docs/html_validation_home.png) |
| Products | ![](docs/html_validation_products.png) |
| Product Detail | ![](docs/html_validation_product_detail.png) |
| Booking Cart | ![](docs/html_validation_bag.png) |
| Checkout | ![](docs/html_validation_checkout.png) |
| Profile | ![](docs/html_validation_profile.png) |
| Login | ![](docs/html_validation_login.png) |
| Sign Up | ![](docs/html_validation_signup.png) |
 
[Back to contents](#contents)
 
---
 
#### CSS
 
CSS was tested using the [W3C CSS Validator (Jigsaw)](https://jigsaw.w3.org/css-validator/).
 
| File | Result |
|------|--------|
| base.css | ![](docs/css_validation.png) |
 
### JavaScript

I have used the recommended [JSHint Validator](https://jshint.com) to validate all of my JavaScript files.

| File | Screenshot | Notes |
| --- | --- | --- |
| stripe_elements.js | ![screenshot](docs/js_validation_stripe.png) | JSHint validation performed using ES11, jQuery and Stripe global configuration |
| bag.html (embedded JS) | ![screenshot](docs/js_validation_bag.png) | JSHint validation performed using ES11 |
| products.html (embedded JS) | ![screenshot](docs/js_validation_products.png) | JSHint validation performed using ES11 |
| product_detail.html (embedded JS) | ![screenshot](docs/js_validation_product_detail.png) | JSHint validation performed using ES11 |
| index.html (embedded JS) | ![screenshot](docs/js_validation_index.png) | JSHint validation performed using ES11, Leaflet global configuration |
 
 
[Back to contents](#contents)
 
---
### Python (PEP8)

I have used the recommended [CI Python Linter](https://pep8ci.herokuapp.com) to validate all of my Python files.

| Directory | File | URL | Screenshot |
| --- | --- | --- | --- |
| bag | contexts.py | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/jolantadjatlova/GlacierGear/refs/heads/main/bag/contexts.py) | ![screenshot](docs/py-bag-contexts.png) |
| bag | urls.py | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/jolantadjatlova/GlacierGear/refs/heads/main/bag/urls.py) | ![screenshot](docs/py-bag-urls.png) |
| bag | views.py | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/jolantadjatlova/GlacierGear/refs/heads/main/bag/views.py) | ![screenshot](docs/py-bag-views.png) |
| bag/templatetags | bag_tools.py | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/jolantadjatlova/GlacierGear/refs/heads/main/bag/templatetags/bag_tools.py) | ![screenshot](docs/py-bag-tools.png) |
| checkout | admin.py | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/jolantadjatlova/GlacierGear/refs/heads/main/checkout/admin.py) | ![screenshot](docs/py-checkout-admin.png) |
| checkout | apps.py | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/jolantadjatlova/GlacierGear/refs/heads/main/checkout/apps.py) | ![screenshot](docs/py-checkout-apps.png) |
| checkout | forms.py | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/jolantadjatlova/GlacierGear/refs/heads/main/checkout/forms.py) | ![screenshot](docs/py-checkout-forms.png) |
| checkout | models.py | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/jolantadjatlova/GlacierGear/refs/heads/main/checkout/models.py) | ![screenshot](docs/py-checkout-models.png) |
| checkout | signals.py | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/jolantadjatlova/GlacierGear/refs/heads/main/checkout/signals.py) | ![screenshot](docs/py-checkout-signals.png) |
| checkout | tests.py | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/jolantadjatlova/GlacierGear/refs/heads/main/checkout/tests.py) | ![screenshot](docs/py-checkout-tests.png) |
| checkout | urls.py | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/jolantadjatlova/GlacierGear/refs/heads/main/checkout/urls.py) | ![screenshot](docs/py-checkout-urls.png) |
| checkout | views.py | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/jolantadjatlova/GlacierGear/refs/heads/main/checkout/views.py) | ![screenshot](docs/py-checkout-views.png) |
| checkout | webhook_handler.py | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/jolantadjatlova/GlacierGear/refs/heads/main/checkout/webhook_handler.py) | ![screenshot](docs/py-checkout-webhook-handler.png) |
| checkout | webhooks.py | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/jolantadjatlova/GlacierGear/refs/heads/main/checkout/webhooks.py) | ![screenshot](docs/py-checkout-webhooks.png) |
| home | tests.py | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/jolantadjatlova/GlacierGear/refs/heads/main/home/tests.py) | ![screenshot](docs/py-home-tests.png) |
| home | urls.py | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/jolantadjatlova/GlacierGear/refs/heads/main/home/urls.py) | ![screenshot](docs/py-home-urls.png) |
| home | views.py | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/jolantadjatlova/GlacierGear/refs/heads/main/home/views.py) | ![screenshot](docs/py-home-views.png) |
| products | admin.py | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/jolantadjatlova/GlacierGear/refs/heads/main/products/admin.py) | ![screenshot](docs/py-products-admin.png) |
| products | apps.py | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/jolantadjatlova/GlacierGear/refs/heads/main/products/apps.py) | ![screenshot](docs/py-products-apps.png) |
| products | forms.py | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/jolantadjatlova/GlacierGear/refs/heads/main/products/forms.py) | ![screenshot](docs/py-products-forms.png) |
| products | models.py | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/jolantadjatlova/GlacierGear/refs/heads/main/products/models.py) | ![screenshot](docs/py-products-models.png) |
| products | signals.py | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/jolantadjatlova/GlacierGear/refs/heads/main/products/signals.py) | ![screenshot](docs/py-products-signals.png) |
| products | tests.py | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/jolantadjatlova/GlacierGear/refs/heads/main/products/tests.py) | ![screenshot](docs/py-products-tests.png) |
| products | urls.py | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/jolantadjatlova/GlacierGear/refs/heads/main/products/urls.py) | ![screenshot](docs/py-products-urls.png) |
| products | views.py | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/jolantadjatlova/GlacierGear/refs/heads/main/products/views.py) | ![screenshot](docs/py-products-views.png) |
| profiles | admin.py | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/jolantadjatlova/GlacierGear/refs/heads/main/profiles/admin.py) | ![screenshot](docs/py-profiles-admin.png) |
| profiles | apps.py | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/jolantadjatlova/GlacierGear/refs/heads/main/profiles/apps.py) | ![screenshot](docs/py-profiles-apps.png) |
| profiles | forms.py | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/jolantadjatlova/GlacierGear/refs/heads/main/profiles/forms.py) | ![screenshot](docs/py-profiles-forms.png) |
| profiles | models.py | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/jolantadjatlova/GlacierGear/refs/heads/main/profiles/models.py) | ![screenshot](docs/py-profiles-models.png) |
| profiles | tests.py | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/jolantadjatlova/GlacierGear/refs/heads/main/profiles/tests.py) | ![screenshot](docs/py-profiles-tests.png) |
| profiles | urls.py | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/jolantadjatlova/GlacierGear/refs/heads/main/profiles/urls.py) | ![screenshot](docs/py-profiles-urls.png) |
| profiles | views.py | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/jolantadjatlova/GlacierGear/refs/heads/main/profiles/views.py) | ![screenshot](docs/py-profiles-views.png) |
| glacier_gear | settings.py | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/jolantadjatlova/GlacierGear/refs/heads/main/glacier_gear/settings.py) | ![screenshot](docs/py-glacier-gear-settings.png) |
| glacier_gear | urls.py | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/jolantadjatlova/GlacierGear/refs/heads/main/glacier_gear/urls.py) | ![screenshot](docs/py-glacier-gear-urls.png) |
| | custom_storages.py | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/jolantadjatlova/GlacierGear/refs/heads/main/custom_storages.py) | ![screenshot](docs/py-custom-storages.png) |
| | manage.py | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/jolantadjatlova/GlacierGear/refs/heads/main/manage.py) | ![screenshot](docs/py-manage.png) |

---
 
### User Story Testing
 
#### Public Users
 
| User Story | Result | Pass | Evidence |
|-----------|--------|------|----------|
| Browse all products without an account | Products page accessible without login | Yes | ![](docs/test_browse_products.png) |
| Filter products by category, size, and colour | Filters apply correctly and update results | Yes | ![](docs/test_filters.png) |
| Search for products by keyword | Search returns relevant results | Yes | ![](docs/test_search.png) |
| View product details including sizes and pricing | Product detail page shows all info | Yes | ![](docs/test_product_detail.png) |
 
#### Authenticated Users
 
| User Story | Result | Pass | Evidence |
|-----------|--------|------|----------|
| Create an account | Registration form works correctly | Yes | ![](docs/test_register.png) |
| Add products to booking cart with rental dates | Items added to cart with correct dates | Yes | ![](docs/test_add_to_cart.png) |
| Complete a secure checkout | Stripe payment processes successfully | Yes | ![](docs/test_checkout.png) |
| Receive a booking confirmation email | Email sent after successful payment | Yes | ![](docs/test_confirmation_email.png) |
| View booking history on profile page | Past bookings listed on profile | Yes | ![](docs/test_booking_history.png) |
 
#### Store Owners
 
| User Story | Result | Pass | Evidence |
|-----------|--------|------|----------|
| Add new products via frontend | Add product form saves correctly | Yes | ![](docs/test_add_product.png) |
| Edit existing products | Edit form pre-fills and saves updates | Yes | ![](docs/test_edit_product.png) |
| Delete products | Delete removes product with confirmation | Yes | ![](docs/test_delete_product.png) |
 
 
[Back to contents](#contents)
 
---
### Feature Testing

| Feature | Expected Outcome | Result | Pass/Fail |
| --- | --- | --- | --- |
| Navbar logo link | Clicking logo returns user to home page | Returns to home page | Pass |
| Navbar product links | Ski Outfits, Snowboard Outfits, Accessories links load correct filtered pages | Correct pages load | Pass |
| Navbar search bar | Searching a keyword returns relevant products | Relevant results displayed | Pass |
| Navbar account dropdown (logged out) | Shows Register and Login links | Correct links shown | Pass |
| Navbar account dropdown (logged in) | Shows My Profile, Product Management (superuser), Logout | Correct links shown | Pass |
| Navbar booking cart icon | Clicking cart icon opens booking cart | Cart page loads | Pass |
| Mobile navbar | Hamburger menu opens and closes correctly | Menu works on mobile | Pass |
| Weather widget | Displays live temperature and description for Borlänge | Live weather shown | Pass |
| Home page category cards | Ski Outfits, Snowboard Outfits, How It Works cards link correctly | Correct pages load | Pass |
| Leaflet map | Interactive map displays pickup location | Map loads correctly | Pass |
| Products page filter | Filtering by gender, garment type, size, colour updates results | Filtered results shown | Pass |
| Products page sort | Sorting by price, name, rating updates order | Sorted results shown | Pass |
| Product card | Image, name, price displayed correctly | All info shown | Pass |
| Product card superuser buttons | Edit and Delete buttons visible to superuser only | Buttons shown to superuser only | Pass |
| Product detail page | Image, description, price, sizes, stock shown correctly | All info displayed | Pass |
| Size selection | Sold out sizes show indicator, low stock warning shown | Correct indicators shown | Pass |
| Date picker | Start and end date can be selected | Dates selectable | Pass |
| Add to cart (logged in) | Item added to cart with correct size and dates | Item added correctly | Pass |
| Add to cart (logged out) | Redirects to login page | Redirect works | Pass |
| Booking cart | Shows items, sizes, dates, quantities, totals | All details shown correctly | Pass |
| Update quantity in cart | Quantity updates correctly and totals recalculate | Update works | Pass |
| Remove item from cart | Item removed and cart updates | Removal works | Pass |
| Checkout form | Pre-fills with saved profile info | Form pre-fills correctly | Pass |
| Checkout save info | Checking save info updates profile on completion | Profile updated | Pass |
| Stripe payment | Valid card processes payment successfully | Payment processes | Pass |
| Stripe payment (invalid card) | Error message shown for invalid card | Error displayed | Pass |
| Checkout success page | Booking reference, details, and line items shown | All details shown | Pass |
| Confirmation email | Email received after successful booking | Email sent | Pass |
| Profile page | Shows email, username, phone number form, booking history | All info displayed | Pass |
| Booking history | Past bookings listed with links to confirmation | History shown correctly | Pass |
| Add product (superuser) | New product saves and appears in store | Product added | Pass |
| Edit product (superuser) | Form pre-fills with existing data and saves updates | Edit works correctly | Pass |
| Delete product (superuser) | Product removed from store | Deletion works | Pass |
| Login | Valid credentials log user in | Login works | Pass |
| Login (invalid) | Error message shown for wrong credentials | Error shown | Pass |
| Register | New account created successfully | Registration works | Pass |
| Logout | User logged out and redirected | Logout works | Pass |
| 404 page | Navigating to invalid URL shows custom 404 page | 404 page shown | Pass |
| 500 page | Server error shows custom 500 page | 500 page shown | Pass |
| Toast notifications | Success/error/info toasts appear for all key actions | Toasts display correctly | Pass |
| CSRF protection | Forms protected against CSRF attacks | Protection active | Pass |


---
 
### Accessibility Testing

Accessibility best practices were applied throughout the site, including:

- Semantic HTML structure
- Clear and consistent navigation
- Appropriate heading hierarchy
- Sufficient colour contrast
- Descriptive alt attributes on all images

The **[WAVE Web Accessibility Evaluation Tool](https://wave.webaim.org/)** was used to evaluate accessibility on key pages.

| Page | Result | Notes |
|------|--------|-------|
| Home | ![](docs/wave_home.png) | 0 errors. 1 contrast error and 1 broken same-page link alert are caused by the third-party Leaflet.js map library and cannot be modified. |
| Products | ![](docs/wave_products.png) | 0 errors. Redundant link and nearby image alerts are due to each product card having both an image link and a View Details button linking to the same product page. |
| Login | ![](docs/wave_login.png) | 0 errors. |
 
### Lighthouse Testing
 
GlacierGear was tested using **Chrome DevTools Lighthouse**.
 
**Mobile:**
 
![Lighthouse Mobile](docs/lighthouse_mobile.png)
 
**Desktop:**
 
![Lighthouse Desktop](docs/lighthouse_desktop.png)
 
 
[Back to contents](#contents)
 
---
 
### Browser Testing
 
| **Browser** | **Pages Tested** | **Result** |
|------------|-----------------|-----------|
| Google Chrome | All pages | Works as expected |
| Mozilla Firefox | All pages | Works as expected |
| Microsoft Edge | All pages | Works as expected |
 
[Back to contents](#contents)
 
---
## Deployment
 
The live deployed application can be found here:
[GlacierGear on Heroku](https://glaciergear-7ce99fc7bac4.herokuapp.com/)
 
### Heroku Deployment
 
This project uses **Heroku** to deploy and host the application.
 
Deployment steps:
 
1. From the Heroku Dashboard, select **New** → **Create new app**.
2. Enter a unique app name, select a region, and click **Create app**.
3. In the app **Settings**, click **Reveal Config Vars** and add the required environment variables.
**Config Vars**
 
| Key | Value |
|---|---|
| `SECRET_KEY` | your Django secret key |
| `DATABASE_URL` | your PostgreSQL database URL |
| `STRIPE_PUBLIC_KEY` | your Stripe public key |
| `STRIPE_SECRET_KEY` | your Stripe secret key |
| `STRIPE_WH_SECRET` | your Stripe webhook signing secret |
| `AWS_ACCESS_KEY_ID` | your AWS IAM access key |
| `AWS_SECRET_ACCESS_KEY` | your AWS IAM secret key |
| `USE_AWS` | `True` |
| `EMAIL_HOST_USER` | your Gmail address (for confirmation emails) |
| `EMAIL_HOST_PASSWORD` | your Gmail app password |
 
4. Ensure the following files exist:
   - `requirements.txt`
   - `Procfile` containing: `web: gunicorn glacier_gear.wsgi`
   - `.python-version`
5. Connect the Heroku app to the GitHub repository in the **Deploy** tab.
6. Deploy from the `main` branch.
7. Run migrations via Heroku console: `python manage.py migrate`
8. Create a superuser: `python manage.py createsuperuser`
---
 
### AWS S3
 
This project uses **Amazon S3** to store static files and media in production.
 
To set up S3:
1. Create an AWS account and navigate to S3.
2. Create a bucket named to match your Heroku app (e.g. `glaciergear-7ce99fc7bac4`).
3. Uncheck "Block all public access" and enable ACLs.
4. Enable static website hosting with `index.html` and `error.html`.
5. Add the CORS configuration and bucket policy (see deployment notes).
6. Create an IAM user group (`glaciergear-staticfiles-group`) with `AmazonS3FullAccess`.
7. Create an IAM user (`glaciergear-staticfiles-user`) and add to the group.
8. Generate access keys and add to Heroku Config Vars as `AWS_ACCESS_KEY_ID` and `AWS_SECRET_ACCESS_KEY`.
9. Add `USE_AWS=True` to Heroku Config Vars.
10. Run `python manage.py collectstatic` to upload static files.
---
### PostgreSQL Database
 
This project uses **PostgreSQL** (via Neon) for the production database.
 
1. Create a PostgreSQL database on [Neon](https://neon.tech/) or another provider.
2. Copy the database URL and add it to:
   - your local `env.py` as `DATABASE_URL`
   - Heroku Config Vars as `DATABASE_URL`
---
### Stripe Payments
 
This project uses **Stripe** for secure payment processing.
 
1. Create a Stripe account and get your public and secret keys.
2. Add them to `env.py` and Heroku Config Vars.
3. Create a webhook endpoint in the Stripe dashboard pointing to:
   `https://glaciergear-7ce99fc7bac4.herokuapp.com/checkout/wh/`
4. Select events: `payment_intent.succeeded` and `payment_intent.payment_failed`.
5. Copy the webhook signing secret and add as `STRIPE_WH_SECRET`.
---
### Local Development
 
#### To Clone the Project
 
1. Go to the [GitHub repository](https://github.com/jolantadjatlova/GlacierGear).
2. Click **Code** and copy the HTTPS link.
3. In your terminal, run: `git clone https://github.com/jolantadjatlova/GlacierGear.git`
4. Install dependencies: `pip install -r requirements.txt`
5. Create an `env.py` file in the project root:
```python
import os
 
os.environ.setdefault("SECRET_KEY", "your-secret-key")
os.environ.setdefault("DEVELOPMENT", "True")
os.environ.setdefault("DATABASE_URL", "your-database-url")
os.environ.setdefault("STRIPE_PUBLIC_KEY", "your-stripe-public-key")
os.environ.setdefault("STRIPE_SECRET_KEY", "your-stripe-secret-key")
os.environ.setdefault("STRIPE_WH_SECRET", "your-stripe-wh-secret")
```
 
6. Run migrations and start the development server:
   - `python manage.py migrate`
   - `python manage.py runserver`
[Back to contents](#contents)
 
---
### To Fork the Project
 
1. Log in to GitHub.
2. Go to [https://github.com/jolantadjatlova/GlacierGear](https://github.com/jolantadjatlova/GlacierGear).
3. Click the **Fork** button in the top right.
4. A copy of the repository will be created in your GitHub account.
[Back to contents](#contents)
 
---
## Credits
 
### Feedback, Advice and Support
 
- Code Institute tutors — for guidance and feedback throughout the project
- Peer support and discussion within the Code Institute Slack community
[Back to contents](#contents)
 
---
 
### Learning Help and Resources
 
- [Code Institute](https://codeinstitute.net/) — Full Stack Frameworks with Django course materials and Boutique Ado walkthrough project
- [Django Documentation](https://docs.djangoproject.com/) — Django framework reference
- [Django Allauth Documentation](https://django-allauth.readthedocs.io/) — Authentication and account management
- [Stripe Documentation](https://stripe.com/docs) — Payment integration and webhooks
- [Open-Meteo Documentation](https://open-meteo.com/en/docs) — Free weather API
- [Leaflet.js Documentation](https://leafletjs.com/) — Interactive map integration
- [AWS S3 Documentation](https://docs.aws.amazon.com/s3/) — Static file storage
- [Real Python](https://realpython.com/) — Python and Django tutorials
- [W3Schools](https://www.w3schools.com/) — Syntax reference
- [Stack Overflow](https://stackoverflow.com/) — Community troubleshooting
[Back to contents](#contents)
 
---
 
### Images
 
- Hero background image sourced from free stock photography.
- Product images sourced from free stock photography sites and uploaded via Django admin.
- GlacierGear logo created for this project.
- All images include descriptive `alt` attributes to support accessibility.
[Back to contents](#contents)
 
---