# Requirement Gathering In LLD

Most LLD failures happen before coding: unclear requirements create confused classes.

## Ask These Questions

- Who are the actors?
- What are the main use cases?
- What is in scope?
- What is out of scope?
- What are the constraints?
- Are there concurrency requirements?
- Are there persistence requirements?
- What should happen on failure?
- What extension points are expected?

## Convert Requirements To Design

Example requirement:

"Users should be able to book movie tickets."

Nouns:

- User
- Movie
- Theatre
- Show
- Seat
- Ticket
- Payment

Verbs:

- search movie
- select show
- lock seat
- make payment
- confirm booking
- cancel booking

Possible classes:

- `User`
- `Movie`
- `Theatre`
- `Show`
- `Seat`
- `Booking`
- `Payment`
- `BookingService`
- `SeatLockService`
