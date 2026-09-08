# EduPay

### A digital platform for tracking and managing student school-fee payments and receipts.

## Project Overview

EduPay is a multi-school digital platform that helps private schools manage, track, and verify students' school-fee payments and receipts in one centralized system.

It gives schools a clearer view of who has paid, who has partially paid, who still owes, and each student's payment history.

## Problem

Many private schools still depend on physical receipts, paper records, and manual payment verification.

This can lead to:

* Lost or delayed payment records.
* Difficulty tracking partial payments.
* Payment disputes between parents and schools.
* Teachers not having up-to-date payment information.
* Students being asked to prove payments they have already made.
* Students missing class while payment is being verified.

## Solution

EduPay provides a centralized digital system where schools can manage students and their payment records.

Schools can:

* Register students and classes.
* Create teacher accounts.
* Assign teachers to classes.
* Record payments.
* Track payment history.
* Calculate outstanding balances.
* See whether a student is **Paid, Partially Paid, or Unpaid**.
* Generate digital receipts.
* Monitor payment information through a dashboard.

## How It Works

### Current MVP

**School → Teacher/Class → Student → Payment Record → Dashboard**

For the MVP, payments are manually/simulated recorded by the school.

Example:

A student's school fee is ₦150,000.

The parent pays ₦75,000.

EduPay records:

**Paid:** ₦75,000
**Balance:** ₦75,000
**Status:** Partially Paid

The updated information is then available on the appropriate school/teacher dashboard.

### Future Payment Flow

When payment infrastructure is integrated:

**Parent → Payment Provider → EduPay → Student Payment Record → School Dashboard**

The payment provider processes the actual transaction, while EduPay receives the payment confirmation and updates the student's record.

## MVP

The first version focuses on:

* School registration
* School ID
* Authentication
* Admin and teacher roles
* Class management
* Student management
* Payment recording
* Payment status
* Balance calculation
* Payment history
* Digital receipts
* School dashboard

## Future Features

* Parent portal
* Online school-fee payments
* Payment gateway integration
* Payment links
* Automatic payment confirmation
* Webhooks
* SMS/email notifications
* AI-powered payment reconciliation
* Advanced reports and analytics
* Multi-campus support

## Target Users

**Schools:** Manage and monitor school-fee payments.

**Teachers:** Quickly verify students' payment status.

**Parents:** Make payments and access receipts and payment history.

**Students:** Experience fewer payment disputes and less disruption to learning.

## Business Model

EduPay can use a **school subscription model**, with different plans based on features and school size.

Future revenue can also come from premium features, payment-related services, and enterprise/custom integrations.

## Technology

**Backend:** Python, Flask, PostgreSQL, SQLAlchemy, Flask-JWT-Extended, Flask-CORS

**Frontend:** To be confirmed

**Deployment:** Render

**Version Control:** Git & GitHub
