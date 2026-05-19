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
  - [User Story Testing](#user-story-testing)
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
- As an authenticated user, I want to save my phone number to my profile so that future checkouts are faster.
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
 
#### JavaScript
 
JavaScript was tested using [JSHint](https://jshint.com/).
 
| File | Result |
|------|--------|
| stripe_elements.js | ![](docs/js_validation_stripe.png) |
| bag.js (quantity/filter scripts) | ![](docs/js_validation_bag.png) |
 
 
[Back to contents](#contents)
 
---
 