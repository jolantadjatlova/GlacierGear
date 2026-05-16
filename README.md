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

