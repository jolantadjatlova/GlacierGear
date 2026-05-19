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