# Chasing Cars – ASCII Animation Project

This project implements a simple ASCII animation that simulates a car chasing a person across a 2D character grid. Each frame is printed sequentially in the terminal to create the appearance of motion. This was developed as part of the CMPE150 – Introduction to Computing course at Boğaziçi University.

## Overview

- The scene consists of two objects: a static human figure and a moving car.
- The car begins on the right side of the frame and moves one column leftward per frame.
- The animation stops once the car has completely exited the frame.
- Each frame is followed by a single empty line.

## Components

### Human Figure
- Head: 4 rows tall, 5 characters wide (`X` border)
- Neck: 1x1
- Arms: 1 row tall, 5 characters wide
- Body: vertical column of height `man_height`
- Legs: predefined shape based on examples

### Car
- A rectangular block of `X` characters with customizable `car_height` and `car_length`
- Appears in front of the human (occludes overlapping parts)

## Input

Inputs are read via predefined variables:

- `car_height`: Height of the car
- `car_length`: Width of the car
- `man_height`: Height of the person's torso (distance between arms and legs)

These are assumed to be:
- Integers greater than the minimum valid size
- Such that `man_height + 5 >= car_height`

## Notes

- No external libraries are used.
- All drawing is handled with standard string manipulation and list-based canvas updates.
- The animation logic respects drawing order and ensures that the car overrides parts of the human figure when overlapping.
- Whitespaces on the right side are ignored during grading.

## Course

CMPE150 – Introduction to Computing  
Boğaziçi University, Fall 2023
