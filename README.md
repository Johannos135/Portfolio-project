## Concert Ticket Sales Application - MVP

This project outlines the Minimum Viable Product (MVP) for a concert ticket sales application.

### Architecture

The application utilizes a n-tier architecture with the following components:

* Client: Web or mobile application for user interaction
* Web Server: Handles API requests and interacts with the database
* Database: Stores application data (users, concerts, tickets, etc.)
* Mobile Money API: Integrates with MTN Mobile Money for secure payments (https://momodeveloper.mtn.com/api-documentation)

### APIs and Methods

The backend provides functionalities through a defined set of API endpoints:

**Public User APIs:**

* GET /api/v1/concerts: Lists concerts with optional filters (artist, date, venue)
* GET /api/v1/concerts/{concert_id}: Retrieves details for a specific concert
* GET /api/v1/users (requires authentication): Retrieves logged-in user information
* GET /api/v1/users/{user_id} (requires authentication and authorization): Retrieves specific user information
* GET /api/v1/tickets (requires authentication): Lists purchased tickets for a user
* GET /api/v1/tickets/{ticket_id}: Retrieves information for a specific ticket
* POST /tickets: Purchases concert tickets
* POST /users: Creates a new user account
* POST /login: Allows user login with credentials

**Admin APIs:**

* POST /admin/concerts: Creates a new concert entry
* PUT /admin/concerts/{concert_id}: Updates information for an existing concert
* PATCH /admin/concerts/{concert_id}/availability: Updates specific details (e.g., available seats)
* GET /admin/concerts: Retrieves a list of all concerts
* GET /admin/concerts/{concert_id}: Retrieves information for a specific concert
* DELETE /admin/concerts/{concert_id} (with restrictions): Deletes a concert

### User Stories

* **User Story 1: User Searches and Purchases Tickets** (As a Music Fan)
    * Users can search for concerts using filters.
    * A list of available concerts with details is displayed.
    * Users can view detailed information for each concert.
    * Users can select and purchase tickets for a concert.
    * The application integrates with Mobile Money for secure payments.
    * Upon successful purchase, users receive confirmation and a ticket ID.

* **User Story 2: User Views Purchase History** (As a Registered User)
    * Users can register and create an account.
    * Registered users can view their past concert ticket purchases.
    * Purchase history lists concerts with details (date, venue, tickets purchased).
    * Users can download or print tickets for each concert.

* **User Story 3: Browse Concerts by Genre or Interest** (As a Music Fan)
    * Users can browse concerts categorized by genre or other criteria.
    * Users can optionally specify preferred genres or artists during registration/profile setup.
    * The application recommends concerts or personalizes search results based on user preferences.

### Authors
    - Johanne ESSIERE
