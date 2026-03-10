-- Axis Finance Database Schema
-- Author: Hoalison Cavalcanti
-- Description: Financial management database for tracking revenue, expenses, debts and goals

CREATE DATABASE IF NOT EXISTS axis_finance;
USE axis_finance;

CREATE TABLE IF NOT EXISTS debts (
    debt_id       INTEGER PRIMARY KEY AUTO_INCREMENT,
    description   TEXT    NOT NULL,
    creditor_name TEXT    NOT NULL,
    creditor_type TEXT    NOT NULL,
    total_amount  REAL    NOT NULL CHECK (total_amount > 0),
    due_date      TEXT    NOT NULL
);

CREATE TABLE IF NOT EXISTS revenue (
    revenue_id  INTEGER PRIMARY KEY AUTO_INCREMENT,
    date        TEXT    NOT NULL,
    source      TEXT    NOT NULL,
    source_type TEXT    NOT NULL,
    amount      REAL    NOT NULL CHECK (amount > 0),
    status      TEXT    NOT NULL CHECK (status = 'received')
);

CREATE TABLE IF NOT EXISTS expenses (
    expenses_id INTEGER PRIMARY KEY AUTO_INCREMENT,
    description TEXT    NOT NULL,
    amount      REAL    NOT NULL CHECK (amount > 0),
    date        TEXT    NOT NULL
);

CREATE TABLE IF NOT EXISTS goals (
    goal_id      INTEGER PRIMARY KEY AUTO_INCREMENT,
    goal_type    TEXT    NOT NULL,
    title        TEXT    NOT NULL,
    target_value REAL    NOT NULL,
    due_date     TEXT
);
