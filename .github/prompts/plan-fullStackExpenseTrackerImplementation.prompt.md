# Full-Stack Expense Tracker — Complete Implementation Guide

Build a complete **Expense Tracker** (React + Express + PostgreSQL) from zero to deployed on Render — every step an enterprise app goes through. You code everything; each phase explains **what**, **why**, and **what to think about before writing a single line**.

---

## Tech Stack

| Layer | Tech | Why |
|---|---|---|
| Backend | Express.js | Minimal, teaches the middleware pattern clearly |
| Database | PostgreSQL + Prisma ORM | Schema-driven dev, real migrations, enterprise standard |
| Frontend | React (Vite) + React Router | Fast, modern, industry default |
| Auth | JWT + bcryptjs | Teaches token-based auth flow end to end |
| Testing | Jest, Supertest, Vitest, React Testing Library | Backend + frontend coverage |
| Containers | Docker + Docker Compose | Run the full stack with one command |
| CI/CD | GitHub Actions | Automated lint → test → build → deploy |
| Hosting | Render (free tier) | Zero infra overhead, focused on learning code |

---

## Phase 0: Project Setup (Day 1)

### Terminal Commands
```bash
# Create repo on GitHub first, then:
mkdir expense-tracker && cd expense-tracker
git init

# Create folder structure
mkdir -p server client docker .github/workflows

# Initialize backend
cd server
npm init -y
cd ..

# Initialize frontend
cd client
npm create vite@latest . -- --template react
cd ..
```

### File: `.gitignore`
```gitignore
node_modules/
dist/
.env
*.log
.DS_Store
coverage/
```

### File: `README.md`
```markdown
# Expense Tracker

Full-stack expense tracking app. React + Express + PostgreSQL.

## Setup

### Prerequisites
- Node.js 20+
- Docker & Docker Compose

### Development
1. `cd server && npm install && npm run dev`
2. `cd client && npm install && npm run dev`

## Architecture
```
Client (React) → API (Express) → Database (PostgreSQL)
```
```

### Commit
```bash
git add .
git commit -m "chore: initial project structure"
```

**Why this matters:** Every enterprise project starts with structure. The monorepo means one PR can touch backend + frontend together. The `.gitignore` protects secrets and junk from ever entering version control.

---

## Phase 1: Backend Skeleton (Day 2)

### Terminal Commands
```bash
cd server
npm install express cors dotenv morgan
```

### File: `server/src/config/index.js`

**Why this file?** Centralize all environment config. If a value changes, you change ONE place.

```js
import dotenv from "dotenv";
dotenv.config();

const config = {
  port: process.env.PORT || 3000,
  nodeEnv: process.env.NODE_ENV || "development",
  clientUrl: process.env.CLIENT_URL || "http://localhost:5173",
};

export default config;
```

### File: `server/src/middleware/errorHandler.js`

**Why this file?** Instead of try/catch in every route, errors bubble here. The 4 parameters (err, req, res, next) tell Express "this is an error handler, not a regular middleware."

```js
const errorHandler = (err, req, res, next) => {
  const status = err.status || 500;
  const message = err.message || "Internal server error";

  console.error(`[ERROR] ${status} - ${message}`);

  res.status(status).json({
    error: {
      message: message,
      status: status,
    },
  });
};

export default errorHandler;
```

### File: `server/src/routes/index.js`

**Why this file?** A single place that registers all route groups. `app.js` just imports this one file.

```js
import { Router } from "express";

const router = Router();

// Health check — every production app has one.
// Load balancers, monitoring tools, and Docker hit this to check if the app is alive.
router.get("/health", (req, res) => {
  res.json({ status: "ok", timestamp: new Date().toISOString() });
});

// Future: router.use('/expenses', expenseRoutes);
// Future: router.use('/auth', authRoutes);

export default router;
```

### File: `server/src/app.js`

**Why separate from server.js?** So tests can import the app WITHOUT starting the HTTP server. This is the #1 pattern professionals use.

```js
import express from "express";
import cors from "cors";
import morgan from "morgan";
import config from "./config/index.js";
import routes from "./routes/index.js";
import errorHandler from "./middleware/errorHandler.js";

const app = express();

// --- Middleware pipeline (ORDER MATTERS) ---

// 1. Logging — see every request in the terminal
app.use(morgan("dev"));

// 2. CORS — allow the React frontend to call this API
app.use(cors({ origin: config.clientUrl }));

// 3. Body parser — converts JSON request bodies to req.body
app.use(express.json());

// 4. Routes — all your endpoints
app.use("/api", routes);

// 5. Error handler — MUST be last. Catches all errors from above.
app.use(errorHandler);

export default app;
```

### File: `server/src/server.js`

```js
import app from "./app.js";
import config from "./config/index.js";

app.listen(config.port, () => {
  console.log(`Server running on http://localhost:${config.port}`);
  console.log(`Environment: ${config.nodeEnv}`);
});
```

### File: `server/.env`
```
PORT=3000
NODE_ENV=development
CLIENT_URL=http://localhost:5173
```

### File: `server/.env.example`
```
PORT=3000
NODE_ENV=development
CLIENT_URL=http://localhost:5173
```

### Update: `server/package.json`

Add `"type": "module"` at the top level and these scripts:

```json
{
  "type": "module",
  "scripts": {
    "dev": "node --watch src/server.js",
    "start": "node src/server.js"
  }
}
```

### Verify
```bash
cd server
npm run dev
# In another terminal:
curl http://localhost:3000/api/health
# Should return: {"status":"ok","timestamp":"..."}
```

### Commit
```bash
git add .
git commit -m "feat: backend skeleton with Express, health check"
```

**Architecture lesson:** The middleware runs in ORDER: logging → CORS → JSON parsing → your routes → error handler. Every request flows through this pipeline. If CORS blocks a request, your route never runs. If your route throws an error, the error handler catches it. This pipeline thinking is how all enterprise backend frameworks work.

---

## Phase 2: Database Setup (Day 3)

### File: `docker-compose.yml` (project root)

**Why Docker for the database?** Never install databases on your machine. Docker means every developer gets the exact same database version, and you can destroy and recreate it in seconds.

```yaml
services:
  postgres:
    image: postgres:16-alpine
    container_name: expense-tracker-db
    environment:
      POSTGRES_USER: expense_user
      POSTGRES_PASSWORD: expense_pass
      POSTGRES_DB: expense_tracker
    ports:
      - "5432:5432"
    volumes:
      - pgdata:/var/lib/postgresql/data

volumes:
  pgdata:
```

### Terminal Commands
```bash
# Start database
docker compose up -d

# Verify it's running
docker compose ps

# Install Prisma
cd server
npm install @prisma/client
npm install prisma --save-dev

# Initialize Prisma
npx prisma init
```

### File: `server/prisma/schema.prisma`

**Why Prisma?** Your database schema is CODE, not something you type into a GUI. Migrations track every change over time — just like git tracks code changes.

```prisma
generator client {
  provider = "prisma-client-js"
}

datasource db {
  provider = "postgresql"
  url      = env("DATABASE_URL")
}

enum Category {
  FOOD
  TRANSPORT
  ENTERTAINMENT
  UTILITIES
  SHOPPING
  HEALTH
  OTHER
}

model User {
  id        Int       @id @default(autoincrement())
  email     String    @unique
  password  String
  name      String
  createdAt DateTime  @default(now())
  expenses  Expense[]
}

model Expense {
  id          Int      @id @default(autoincrement())
  amount      Decimal  @db.Decimal(10, 2)
  category    Category
  description String   @db.VarChar(200)
  date        DateTime
  createdAt   DateTime @default(now())
  updatedAt   DateTime @updatedAt
  userId      Int
  user        User     @relation(fields: [userId], references: [id])

  @@index([userId, date(sort: Desc)])
}
```

### Update: `server/.env`

Add the database URL:
```
DATABASE_URL="postgresql://expense_user:expense_pass@localhost:5432/expense_tracker"
```

### File: `server/src/lib/prisma.js`

**Why a singleton?** Creating a new Prisma client per request opens a new database connection pool each time — this crashes your database. One client, reused everywhere.

```js
import { PrismaClient } from "@prisma/client";

const prisma = new PrismaClient();

export default prisma;
```

### File: `server/prisma/seed.js`

```js
import { PrismaClient } from "@prisma/client";
import bcrypt from "bcryptjs";

const prisma = new PrismaClient();

async function main() {
  // Create a test user (password: "password123")
  const hashedPassword = await bcrypt.hash("password123", 10);

  const user = await prisma.user.upsert({
    where: { email: "test@example.com" },
    update: {},
    create: {
      email: "test@example.com",
      password: hashedPassword,
      name: "Test User",
    },
  });

  // Create sample expenses
  const expenses = [
    { amount: 12.50, category: "FOOD", description: "Lunch at cafe", date: new Date("2026-04-01") },
    { amount: 45.00, category: "TRANSPORT", description: "Gas fill-up", date: new Date("2026-04-02") },
    { amount: 9.99, category: "ENTERTAINMENT", description: "Movie ticket", date: new Date("2026-04-03") },
    { amount: 85.00, category: "UTILITIES", description: "Electric bill", date: new Date("2026-04-05") },
    { amount: 32.50, category: "SHOPPING", description: "T-shirt", date: new Date("2026-04-07") },
    { amount: 20.00, category: "HEALTH", description: "Pharmacy", date: new Date("2026-04-08") },
    { amount: 150.00, category: "OTHER", description: "Birthday gift", date: new Date("2026-04-10") },
  ];

  for (const expense of expenses) {
    await prisma.expense.create({
      data: {
        ...expense,
        userId: user.id,
      },
    });
  }

  console.log("Seed complete: 1 user, 7 expenses");
}

main()
  .catch(console.error)
  .finally(() => prisma.$disconnect());
```

### Terminal Commands
```bash
cd server
npm install bcryptjs   # needed for seed

# Run migration
npx prisma migrate dev --name init

# Seed the database
node prisma/seed.js

# Open Prisma Studio to see your data
npx prisma studio
```

### Update: `server/package.json` — add prisma seed config:
```json
{
  "prisma": {
    "seed": "node prisma/seed.js"
  }
}
```

### Commit
```bash
git add .
git commit -m "feat: PostgreSQL setup, Prisma schema, seed data"
```

**Architecture lesson:** The `@@index([userId, date(sort: Desc)])` is a **composite index**. When you query "give me user 5's expenses sorted by date," PostgreSQL doesn't scan every row — it jumps straight to user 5's entries, already sorted. Without this, queries slow down exponentially as data grows. This is the #1 thing that separates toy projects from production apps.

---

## Phase 3: REST API — Expenses CRUD (Day 4–5)

### File: `server/src/services/expenseService.js`

**Why a service layer?** The service contains business logic and data access. It knows NOTHING about HTTP — no `req`, no `res`. This means you could call the same service from a CLI tool, a WebSocket handler, or a cron job.

```js
import prisma from "../lib/prisma.js";

// List expenses with filtering + pagination
async function getAll(userId, { category, startDate, endDate, page = 1, limit = 10 }) {
  const where = { userId };

  if (category) {
    where.category = category;
  }

  if (startDate || endDate) {
    where.date = {};
    if (startDate) where.date.gte = new Date(startDate);
    if (endDate) where.date.lte = new Date(endDate);
  }

  const skip = (page - 1) * limit;

  const [expenses, total] = await Promise.all([
    prisma.expense.findMany({
      where,
      orderBy: { date: "desc" },
      skip,
      take: limit,
    }),
    prisma.expense.count({ where }),
  ]);

  return {
    expenses,
    pagination: {
      page,
      limit,
      total,
      totalPages: Math.ceil(total / limit),
    },
  };
}

// Get single expense — MUST check userId to prevent IDOR
async function getById(id, userId) {
  const expense = await prisma.expense.findFirst({
    where: { id: Number(id), userId },
  });

  if (!expense) {
    const error = new Error("Expense not found");
    error.status = 404;
    throw error;
  }

  return expense;
}

// Create expense
async function create(userId, data) {
  return prisma.expense.create({
    data: {
      amount: data.amount,
      category: data.category,
      description: data.description,
      date: new Date(data.date),
      userId,
    },
  });
}

// Update expense — MUST verify ownership
async function update(id, userId, data) {
  // First verify the expense belongs to this user
  await getById(id, userId);

  return prisma.expense.update({
    where: { id: Number(id) },
    data: {
      amount: data.amount,
      category: data.category,
      description: data.description,
      date: data.date ? new Date(data.date) : undefined,
    },
  });
}

// Delete expense — MUST verify ownership
async function remove(id, userId) {
  await getById(id, userId);
  return prisma.expense.delete({ where: { id: Number(id) } });
}

// Dashboard summary — aggregate stats for one user
async function getSummary(userId) {
  const [totals, byCategory, monthly] = await Promise.all([
    // Total spent
    prisma.expense.aggregate({
      where: { userId },
      _sum: { amount: true },
      _count: { id: true },
    }),

    // Breakdown by category
    prisma.expense.groupBy({
      by: ["category"],
      where: { userId },
      _sum: { amount: true },
      _count: { id: true },
    }),

    // Monthly totals (last 6 months)
    prisma.$queryRaw`
      SELECT
        TO_CHAR(date, 'YYYY-MM') as month,
        SUM(amount)::float as total,
        COUNT(*)::int as count
      FROM "Expense"
      WHERE "userId" = ${userId}
        AND date >= NOW() - INTERVAL '6 months'
      GROUP BY TO_CHAR(date, 'YYYY-MM')
      ORDER BY month DESC
    `,
  ]);

  return {
    totalSpent: totals._sum.amount || 0,
    totalCount: totals._count.id,
    byCategory,
    monthly,
  };
}

export default { getAll, getById, create, update, remove, getSummary };
```

### File: `server/src/middleware/validate.js`

**Why validate on the server?** The frontend can be bypassed — anyone can send a curl request directly to your API. Server validation is the REAL security boundary.

```js
const VALID_CATEGORIES = [
  "FOOD", "TRANSPORT", "ENTERTAINMENT", "UTILITIES", "SHOPPING", "HEALTH", "OTHER",
];

function validateExpense(req, res, next) {
  const errors = [];
  const { amount, category, description, date } = req.body;

  if (amount === undefined || amount === null) {
    errors.push("Amount is required");
  } else if (typeof amount !== "number" || amount <= 0) {
    errors.push("Amount must be a positive number");
  }

  if (!category) {
    errors.push("Category is required");
  } else if (!VALID_CATEGORIES.includes(category)) {
    errors.push(`Category must be one of: ${VALID_CATEGORIES.join(", ")}`);
  }

  if (!description) {
    errors.push("Description is required");
  } else if (description.length > 200) {
    errors.push("Description must be 200 characters or less");
  }

  if (!date) {
    errors.push("Date is required");
  } else if (isNaN(new Date(date).getTime())) {
    errors.push("Date must be a valid ISO date string");
  }

  if (errors.length > 0) {
    return res.status(400).json({ error: { message: "Validation failed", details: errors } });
  }

  next();
}

export { validateExpense };
```

### File: `server/src/controllers/expenseController.js`

**Why a controller layer?** The controller knows about HTTP (req/res) but delegates all real work to the service. It's the translator between "HTTP world" and "business logic world."

```js
import expenseService from "../services/expenseService.js";

async function getAll(req, res, next) {
  try {
    const filters = {
      category: req.query.category,
      startDate: req.query.startDate,
      endDate: req.query.endDate,
      page: parseInt(req.query.page) || 1,
      limit: parseInt(req.query.limit) || 10,
    };

    const result = await expenseService.getAll(req.userId, filters);
    res.json(result);
  } catch (err) {
    next(err);
  }
}

async function getById(req, res, next) {
  try {
    const expense = await expenseService.getById(req.params.id, req.userId);
    res.json(expense);
  } catch (err) {
    next(err);
  }
}

async function create(req, res, next) {
  try {
    const expense = await expenseService.create(req.userId, req.body);
    res.status(201).json(expense);
  } catch (err) {
    next(err);
  }
}

async function update(req, res, next) {
  try {
    const expense = await expenseService.update(req.params.id, req.userId, req.body);
    res.json(expense);
  } catch (err) {
    next(err);
  }
}

async function remove(req, res, next) {
  try {
    await expenseService.remove(req.params.id, req.userId);
    res.status(204).end();
  } catch (err) {
    next(err);
  }
}

async function getSummary(req, res, next) {
  try {
    const summary = await expenseService.getSummary(req.userId);
    res.json(summary);
  } catch (err) {
    next(err);
  }
}

export default { getAll, getById, create, update, remove, getSummary };
```

### File: `server/src/routes/expenses.js`

```js
import { Router } from "express";
import expenseController from "../controllers/expenseController.js";
import { validateExpense } from "../middleware/validate.js";

const router = Router();

router.get("/",        expenseController.getAll);
router.get("/summary", expenseController.getSummary);
router.get("/:id",     expenseController.getById);
router.post("/",       validateExpense, expenseController.create);
router.put("/:id",     validateExpense, expenseController.update);
router.delete("/:id",  expenseController.remove);

export default router;
```

### Update: `server/src/routes/index.js`

```js
import { Router } from "express";
import expenseRoutes from "./expenses.js";

const router = Router();

router.get("/health", (req, res) => {
  res.json({ status: "ok", timestamp: new Date().toISOString() });
});

// For now, use a temporary middleware that fakes a userId.
// We'll replace this with real auth in Phase 6.
router.use("/expenses", (req, res, next) => {
  req.userId = 1; // Temporary — hardcoded user ID from seed data
  next();
}, expenseRoutes);

export default router;
```

### Verify with curl
```bash
# List expenses
curl http://localhost:3000/api/expenses

# Get summary
curl http://localhost:3000/api/expenses/summary

# Create expense
curl -X POST http://localhost:3000/api/expenses \
  -H "Content-Type: application/json" \
  -d '{"amount": 25.50, "category": "FOOD", "description": "Pizza", "date": "2026-04-11"}'

# Update expense (use the id from the create response)
curl -X PUT http://localhost:3000/api/expenses/1 \
  -H "Content-Type: application/json" \
  -d '{"amount": 30.00, "category": "FOOD", "description": "Pizza and drink", "date": "2026-04-11"}'

# Delete expense
curl -X DELETE http://localhost:3000/api/expenses/8

# Test validation — should return 400
curl -X POST http://localhost:3000/api/expenses \
  -H "Content-Type: application/json" \
  -d '{"amount": -5, "category": "INVALID"}'
```

### Commit
```bash
git add .
git commit -m "feat: expenses CRUD API with validation and service layer"
```

**Architecture lesson:** Notice the **3-layer flow**: Route (HTTP routing) → Controller (translate req/res) → Service (business logic + database). If you switch from Express to Fastify tomorrow, only the controllers change. If you switch from PostgreSQL to MongoDB, only the service changes. This layered separation is how enterprise codebases stay maintainable at 100k+ lines of code.

---

## Phase 4: Frontend Setup (Day 6)

### Terminal Commands
```bash
cd client
npm install react-router-dom
```

### File: `client/.env`
```
VITE_API_URL=http://localhost:3000/api
```

### File: `client/.env.example`
```
VITE_API_URL=http://localhost:3000/api
```

### File: `client/src/api/expenses.js`

**Why this file?** Every API call goes through here. If the backend URL changes, or you need to add auth headers, you change ONE file — not 20 components.

```js
const API_URL = import.meta.env.VITE_API_URL;

async function request(endpoint, options = {}) {
  const config = {
    headers: {
      "Content-Type": "application/json",
    },
    ...options,
  };

  // We'll add auth token here in Phase 6
  const token = localStorage.getItem("token");
  if (token) {
    config.headers.Authorization = `Bearer ${token}`;
  }

  const response = await fetch(`${API_URL}${endpoint}`, config);

  if (!response.ok) {
    const error = await response.json().catch(() => ({ error: { message: "Network error" } }));
    throw new Error(error.error?.message || `HTTP ${response.status}`);
  }

  // 204 No Content has no body
  if (response.status === 204) return null;

  return response.json();
}

export function getExpenses(filters = {}) {
  const params = new URLSearchParams();
  if (filters.category) params.set("category", filters.category);
  if (filters.page) params.set("page", filters.page);
  if (filters.limit) params.set("limit", filters.limit);

  const query = params.toString();
  return request(`/expenses${query ? `?${query}` : ""}`);
}

export function getExpense(id) {
  return request(`/expenses/${id}`);
}

export function createExpense(data) {
  return request("/expenses", { method: "POST", body: JSON.stringify(data) });
}

export function updateExpense(id, data) {
  return request(`/expenses/${id}`, { method: "PUT", body: JSON.stringify(data) });
}

export function deleteExpense(id) {
  return request(`/expenses/${id}`, { method: "DELETE" });
}

export function getSummary() {
  return request("/expenses/summary");
}
```

### File: `client/src/api/auth.js`

Prepare this now, we'll use it in Phase 6:

```js
const API_URL = import.meta.env.VITE_API_URL;

async function request(endpoint, options = {}) {
  const response = await fetch(`${API_URL}${endpoint}`, {
    headers: { "Content-Type": "application/json" },
    ...options,
  });

  const data = await response.json().catch(() => ({}));

  if (!response.ok) {
    throw new Error(data.error?.message || `HTTP ${response.status}`);
  }

  return data;
}

export function login(email, password) {
  return request("/auth/login", { method: "POST", body: JSON.stringify({ email, password }) });
}

export function signup(email, password, name) {
  return request("/auth/signup", { method: "POST", body: JSON.stringify({ email, password, name }) });
}

export function getMe() {
  const token = localStorage.getItem("token");
  return request("/auth/me", {
    headers: {
      "Content-Type": "application/json",
      Authorization: `Bearer ${token}`,
    },
  });
}
```

### File: `client/src/components/Layout.jsx`

```jsx
import { Link, Outlet } from "react-router-dom";

export default function Layout() {
  return (
    <div className="app">
      <nav className="navbar">
        <Link to="/" className="nav-brand">💰 Expense Tracker</Link>
        <div className="nav-links">
          <Link to="/expenses">Expenses</Link>
          <Link to="/dashboard">Dashboard</Link>
          <Link to="/login">Login</Link>
        </div>
      </nav>
      <main className="container">
        <Outlet />
      </main>
    </div>
  );
}
```

### File: `client/src/pages/HomePage.jsx`

```jsx
import { Link } from "react-router-dom";

export default function HomePage() {
  return (
    <div className="home">
      <h1>Expense Tracker</h1>
      <p>Track your spending. Understand your habits. Save more.</p>
      <div className="home-actions">
        <Link to="/expenses" className="btn btn-primary">View Expenses</Link>
        <Link to="/dashboard" className="btn">Dashboard</Link>
      </div>
    </div>
  );
}
```

### File: `client/src/pages/ExpensesPage.jsx` (placeholder — built out in Phase 5)

```jsx
export default function ExpensesPage() {
  return <h1>Expenses — coming in Phase 5</h1>;
}
```

### File: `client/src/pages/DashboardPage.jsx` (placeholder)

```jsx
export default function DashboardPage() {
  return <h1>Dashboard — coming in Phase 5</h1>;
}
```

### File: `client/src/pages/LoginPage.jsx` (placeholder)

```jsx
export default function LoginPage() {
  return <h1>Login — coming in Phase 6</h1>;
}
```

### File: `client/src/pages/SignupPage.jsx` (placeholder)

```jsx
export default function SignupPage() {
  return <h1>Signup — coming in Phase 6</h1>;
}
```

### File: `client/src/App.jsx`

```jsx
import { BrowserRouter, Routes, Route } from "react-router-dom";
import Layout from "./components/Layout";
import HomePage from "./pages/HomePage";
import ExpensesPage from "./pages/ExpensesPage";
import DashboardPage from "./pages/DashboardPage";
import LoginPage from "./pages/LoginPage";
import SignupPage from "./pages/SignupPage";

export default function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Layout />}>
          <Route index element={<HomePage />} />
          <Route path="expenses" element={<ExpensesPage />} />
          <Route path="dashboard" element={<DashboardPage />} />
          <Route path="login" element={<LoginPage />} />
          <Route path="signup" element={<SignupPage />} />
        </Route>
      </Routes>
    </BrowserRouter>
  );
}
```

### File: `client/src/index.css`

```css
/* ===== Reset & Base ===== */
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

body {
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
  background: #f5f5f5;
  color: #333;
  line-height: 1.6;
}

/* ===== Layout ===== */
.navbar {
  background: #1a1a2e;
  color: white;
  padding: 1rem 2rem;
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.nav-brand {
  color: white;
  text-decoration: none;
  font-size: 1.25rem;
  font-weight: bold;
}

.nav-links {
  display: flex;
  gap: 1.5rem;
}

.nav-links a {
  color: #ccc;
  text-decoration: none;
}

.nav-links a:hover {
  color: white;
}

.container {
  max-width: 900px;
  margin: 2rem auto;
  padding: 0 1rem;
}

/* ===== Buttons ===== */
.btn {
  display: inline-block;
  padding: 0.5rem 1.25rem;
  border: 1px solid #ccc;
  border-radius: 4px;
  text-decoration: none;
  color: #333;
  background: white;
  cursor: pointer;
  font-size: 0.9rem;
}

.btn-primary {
  background: #4361ee;
  color: white;
  border-color: #4361ee;
}

.btn-danger {
  background: #e63946;
  color: white;
  border-color: #e63946;
}

.btn:hover {
  opacity: 0.85;
}

/* ===== Home ===== */
.home {
  text-align: center;
  padding: 4rem 0;
}

.home h1 {
  font-size: 2.5rem;
  margin-bottom: 0.5rem;
}

.home-actions {
  margin-top: 2rem;
  display: flex;
  gap: 1rem;
  justify-content: center;
}

/* ===== Forms ===== */
.form-group {
  margin-bottom: 1rem;
}

.form-group label {
  display: block;
  margin-bottom: 0.25rem;
  font-weight: 600;
  font-size: 0.85rem;
}

.form-group input,
.form-group select,
.form-group textarea {
  width: 100%;
  padding: 0.5rem;
  border: 1px solid #ccc;
  border-radius: 4px;
  font-size: 0.9rem;
}

/* ===== Cards ===== */
.card {
  background: white;
  border-radius: 8px;
  padding: 1rem 1.25rem;
  margin-bottom: 0.75rem;
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.08);
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.card-info h3 {
  font-size: 1rem;
  margin-bottom: 0.25rem;
}

.card-info p {
  color: #666;
  font-size: 0.85rem;
}

.card-amount {
  font-size: 1.25rem;
  font-weight: 700;
  color: #e63946;
}

.card-actions {
  display: flex;
  gap: 0.5rem;
  margin-left: 1rem;
}

/* ===== Category Badge ===== */
.badge {
  display: inline-block;
  padding: 0.15rem 0.5rem;
  border-radius: 12px;
  font-size: 0.7rem;
  font-weight: 600;
  text-transform: uppercase;
  background: #e2e8f0;
}

/* ===== Dashboard ===== */
.stats-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  gap: 1rem;
  margin-bottom: 2rem;
}

.stat-card {
  background: white;
  border-radius: 8px;
  padding: 1.5rem;
  text-align: center;
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.08);
}

.stat-card h3 {
  color: #666;
  font-size: 0.85rem;
  margin-bottom: 0.5rem;
}

.stat-card .stat-value {
  font-size: 2rem;
  font-weight: 700;
  color: #1a1a2e;
}

/* ===== Filters ===== */
.filters {
  display: flex;
  gap: 1rem;
  margin-bottom: 1.5rem;
  flex-wrap: wrap;
}

/* ===== Error & Loading ===== */
.error {
  color: #e63946;
  background: #ffeef0;
  padding: 0.75rem;
  border-radius: 4px;
  margin-bottom: 1rem;
}

.loading {
  text-align: center;
  color: #666;
  padding: 2rem;
}

/* ===== Auth Forms ===== */
.auth-form {
  max-width: 400px;
  margin: 2rem auto;
  background: white;
  padding: 2rem;
  border-radius: 8px;
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.08);
}

.auth-form h1 {
  margin-bottom: 1.5rem;
}
```

### Update: `client/src/main.jsx`

```jsx
import { StrictMode } from "react";
import { createRoot } from "react-dom/client";
import App from "./App.jsx";
import "./index.css";

createRoot(document.getElementById("root")).render(
  <StrictMode>
    <App />
  </StrictMode>
);
```

### Verify
```bash
cd client
npm run dev
# Visit http://localhost:5173 — nav should work, pages show placeholders
```

### Commit
```bash
git add .
git commit -m "feat: React frontend with routing, API layer, and base styles"
```

---

## Phase 5: Frontend UI — Full Experience (Day 7–8)

### File: `client/src/hooks/useExpenses.js`

**Why a custom hook?** Extracts ALL data-fetching logic from the page component. The page becomes simple — it just renders what the hook gives it. This is the React pattern used by every professional codebase.

```jsx
import { useState, useEffect, useCallback } from "react";
import { getExpenses, createExpense, updateExpense, deleteExpense } from "../api/expenses";

export default function useExpenses() {
  const [expenses, setExpenses] = useState([]);
  const [pagination, setPagination] = useState({});
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  const [filters, setFilters] = useState({ category: "", page: 1, limit: 10 });

  const fetchExpenses = useCallback(async () => {
    try {
      setLoading(true);
      setError(null);
      const data = await getExpenses(filters);
      setExpenses(data.expenses);
      setPagination(data.pagination);
    } catch (err) {
      setError(err.message);
    } finally {
      setLoading(false);
    }
  }, [filters]);

  useEffect(() => {
    fetchExpenses();
  }, [fetchExpenses]);

  async function addExpense(data) {
    const created = await createExpense(data);
    await fetchExpenses(); // Refetch to stay in sync with server
    return created;
  }

  async function editExpense(id, data) {
    const updated = await updateExpense(id, data);
    await fetchExpenses();
    return updated;
  }

  async function removeExpense(id) {
    await deleteExpense(id);
    await fetchExpenses();
  }

  return {
    expenses,
    pagination,
    loading,
    error,
    filters,
    setFilters,
    addExpense,
    editExpense,
    removeExpense,
  };
}
```

### File: `client/src/components/ExpenseCard.jsx`

**Dumb component** — receives data via props, calls callbacks when buttons are clicked. Knows nothing about APIs or state.

```jsx
export default function ExpenseCard({ expense, onEdit, onDelete }) {
  return (
    <div className="card">
      <div className="card-info">
        <h3>{expense.description}</h3>
        <p>
          <span className="badge">{expense.category}</span>
          {" · "}
          {new Date(expense.date).toLocaleDateString()}
        </p>
      </div>
      <div style={{ display: "flex", alignItems: "center" }}>
        <span className="card-amount">${Number(expense.amount).toFixed(2)}</span>
        <div className="card-actions">
          <button className="btn" onClick={() => onEdit(expense)}>Edit</button>
          <button className="btn btn-danger" onClick={() => onDelete(expense.id)}>Delete</button>
        </div>
      </div>
    </div>
  );
}
```

### File: `client/src/components/ExpenseList.jsx`

```jsx
import ExpenseCard from "./ExpenseCard";

export default function ExpenseList({ expenses, loading, error, onEdit, onDelete }) {
  if (loading) return <div className="loading">Loading expenses...</div>;
  if (error) return <div className="error">{error}</div>;
  if (expenses.length === 0) return <div className="loading">No expenses yet. Add one!</div>;

  return (
    <div>
      {expenses.map((expense) => (
        <ExpenseCard
          key={expense.id}
          expense={expense}
          onEdit={onEdit}
          onDelete={onDelete}
        />
      ))}
    </div>
  );
}
```

### File: `client/src/components/ExpenseForm.jsx`

**Works for BOTH create and edit.** If `expense` prop is passed, it pre-fills the form. This is how you avoid duplicating form code.

```jsx
import { useState, useEffect } from "react";

const CATEGORIES = ["FOOD", "TRANSPORT", "ENTERTAINMENT", "UTILITIES", "SHOPPING", "HEALTH", "OTHER"];

export default function ExpenseForm({ expense, onSubmit, onCancel }) {
  const [form, setForm] = useState({
    amount: "",
    category: "FOOD",
    description: "",
    date: new Date().toISOString().split("T")[0],
  });
  const [error, setError] = useState("");

  // If editing, pre-fill the form
  useEffect(() => {
    if (expense) {
      setForm({
        amount: expense.amount,
        category: expense.category,
        description: expense.description,
        date: new Date(expense.date).toISOString().split("T")[0],
      });
    }
  }, [expense]);

  function handleChange(e) {
    setForm({ ...form, [e.target.name]: e.target.value });
  }

  async function handleSubmit(e) {
    e.preventDefault();
    setError("");

    // Client-side validation
    if (!form.amount || Number(form.amount) <= 0) {
      setError("Amount must be a positive number");
      return;
    }
    if (!form.description.trim()) {
      setError("Description is required");
      return;
    }

    try {
      await onSubmit({
        amount: Number(form.amount),
        category: form.category,
        description: form.description.trim(),
        date: form.date,
      });

      // Reset form after successful create (not edit)
      if (!expense) {
        setForm({
          amount: "",
          category: "FOOD",
          description: "",
          date: new Date().toISOString().split("T")[0],
        });
      }
    } catch (err) {
      setError(err.message);
    }
  }

  return (
    <form onSubmit={handleSubmit} className="auth-form" style={{ margin: "0 0 1.5rem 0", maxWidth: "100%" }}>
      <h2>{expense ? "Edit Expense" : "Add Expense"}</h2>
      {error && <div className="error">{error}</div>}

      <div className="form-group">
        <label>Amount ($)</label>
        <input type="number" name="amount" step="0.01" value={form.amount} onChange={handleChange} />
      </div>

      <div className="form-group">
        <label>Category</label>
        <select name="category" value={form.category} onChange={handleChange}>
          {CATEGORIES.map((cat) => (
            <option key={cat} value={cat}>{cat}</option>
          ))}
        </select>
      </div>

      <div className="form-group">
        <label>Description</label>
        <input type="text" name="description" maxLength={200} value={form.description} onChange={handleChange} />
      </div>

      <div className="form-group">
        <label>Date</label>
        <input type="date" name="date" value={form.date} onChange={handleChange} />
      </div>

      <div style={{ display: "flex", gap: "0.5rem" }}>
        <button type="submit" className="btn btn-primary">{expense ? "Save" : "Add"}</button>
        {onCancel && <button type="button" className="btn" onClick={onCancel}>Cancel</button>}
      </div>
    </form>
  );
}
```

### File: `client/src/components/CategoryFilter.jsx`

```jsx
const CATEGORIES = ["", "FOOD", "TRANSPORT", "ENTERTAINMENT", "UTILITIES", "SHOPPING", "HEALTH", "OTHER"];

export default function CategoryFilter({ value, onChange }) {
  return (
    <div className="filters">
      <select value={value} onChange={(e) => onChange(e.target.value)}>
        <option value="">All Categories</option>
        {CATEGORIES.filter(Boolean).map((cat) => (
          <option key={cat} value={cat}>{cat}</option>
        ))}
      </select>
    </div>
  );
}
```

### File: `client/src/pages/ExpensesPage.jsx` (replace placeholder)

**Smart component** — manages state via the custom hook, passes data down to dumb components.

```jsx
import { useState } from "react";
import useExpenses from "../hooks/useExpenses";
import ExpenseList from "../components/ExpenseList";
import ExpenseForm from "../components/ExpenseForm";
import CategoryFilter from "../components/CategoryFilter";

export default function ExpensesPage() {
  const {
    expenses, pagination, loading, error,
    filters, setFilters, addExpense, editExpense, removeExpense,
  } = useExpenses();
  const [editing, setEditing] = useState(null);
  const [showForm, setShowForm] = useState(false);

  async function handleSubmit(data) {
    if (editing) {
      await editExpense(editing.id, data);
      setEditing(null);
    } else {
      await addExpense(data);
    }
    setShowForm(false);
  }

  function handleEdit(expense) {
    setEditing(expense);
    setShowForm(true);
  }

  function handleCancel() {
    setEditing(null);
    setShowForm(false);
  }

  async function handleDelete(id) {
    if (window.confirm("Delete this expense?")) {
      await removeExpense(id);
    }
  }

  return (
    <div>
      <div style={{ display: "flex", justifyContent: "space-between", alignItems: "center", marginBottom: "1rem" }}>
        <h1>Expenses</h1>
        <button className="btn btn-primary" onClick={() => { setEditing(null); setShowForm(!showForm); }}>
          {showForm ? "Close" : "+ Add Expense"}
        </button>
      </div>

      {showForm && (
        <ExpenseForm expense={editing} onSubmit={handleSubmit} onCancel={handleCancel} />
      )}

      <CategoryFilter
        value={filters.category}
        onChange={(category) => setFilters({ ...filters, category, page: 1 })}
      />

      <ExpenseList
        expenses={expenses}
        loading={loading}
        error={error}
        onEdit={handleEdit}
        onDelete={handleDelete}
      />

      {/* Pagination */}
      {pagination.totalPages > 1 && (
        <div style={{ display: "flex", gap: "0.5rem", justifyContent: "center", marginTop: "1rem" }}>
          <button
            className="btn"
            disabled={filters.page <= 1}
            onClick={() => setFilters({ ...filters, page: filters.page - 1 })}
          >
            Previous
          </button>
          <span style={{ padding: "0.5rem" }}>
            Page {pagination.page} of {pagination.totalPages}
          </span>
          <button
            className="btn"
            disabled={filters.page >= pagination.totalPages}
            onClick={() => setFilters({ ...filters, page: filters.page + 1 })}
          >
            Next
          </button>
        </div>
      )}
    </div>
  );
}
```

### File: `client/src/components/Dashboard.jsx`

```jsx
import { useState, useEffect } from "react";
import { getSummary } from "../api/expenses";

export default function Dashboard() {
  const [summary, setSummary] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    async function fetchSummary() {
      try {
        const data = await getSummary();
        setSummary(data);
      } catch (err) {
        setError(err.message);
      } finally {
        setLoading(false);
      }
    }
    fetchSummary();
  }, []);

  if (loading) return <div className="loading">Loading dashboard...</div>;
  if (error) return <div className="error">{error}</div>;

  return (
    <div>
      {/* Top-level stats */}
      <div className="stats-grid">
        <div className="stat-card">
          <h3>Total Spent</h3>
          <div className="stat-value">${Number(summary.totalSpent).toFixed(2)}</div>
        </div>
        <div className="stat-card">
          <h3>Total Expenses</h3>
          <div className="stat-value">{summary.totalCount}</div>
        </div>
        <div className="stat-card">
          <h3>Average</h3>
          <div className="stat-value">
            ${summary.totalCount > 0
              ? (Number(summary.totalSpent) / summary.totalCount).toFixed(2)
              : "0.00"}
          </div>
        </div>
      </div>

      {/* By Category */}
      <h2 style={{ marginBottom: "1rem" }}>By Category</h2>
      {summary.byCategory.map((cat) => (
        <div key={cat.category} className="card">
          <div className="card-info">
            <h3><span className="badge">{cat.category}</span></h3>
            <p>{cat._count.id} expense{cat._count.id !== 1 ? "s" : ""}</p>
          </div>
          <span className="card-amount">${Number(cat._sum.amount).toFixed(2)}</span>
        </div>
      ))}

      {/* Monthly */}
      {summary.monthly.length > 0 && (
        <>
          <h2 style={{ margin: "2rem 0 1rem" }}>Monthly Totals</h2>
          {summary.monthly.map((m) => (
            <div key={m.month} className="card">
              <div className="card-info">
                <h3>{m.month}</h3>
                <p>{m.count} expense{m.count !== 1 ? "s" : ""}</p>
              </div>
              <span className="card-amount">${Number(m.total).toFixed(2)}</span>
            </div>
          ))}
        </>
      )}
    </div>
  );
}
```

### File: `client/src/pages/DashboardPage.jsx` (replace placeholder)

```jsx
import Dashboard from "../components/Dashboard";

export default function DashboardPage() {
  return (
    <div>
      <h1 style={{ marginBottom: "1.5rem" }}>Dashboard</h1>
      <Dashboard />
    </div>
  );
}
```

### Verify
```bash
# Make sure backend is running: cd server && npm run dev
# Make sure frontend is running: cd client && npm run dev
# Visit http://localhost:5173/expenses — CRUD should work
# Visit http://localhost:5173/dashboard — summary should show
```

### Commit
```bash
git add .
git commit -m "feat: full expenses UI with CRUD, filtering, pagination, dashboard"
```

---

## Phase 6: Authentication (Day 9–10)

### Terminal Commands
```bash
cd server
npm install jsonwebtoken bcryptjs
```

(bcryptjs may already be installed from the seed step — that's fine.)

### File: `server/src/services/authService.js`

```js
import bcrypt from "bcryptjs";
import jwt from "jsonwebtoken";
import prisma from "../lib/prisma.js";
import config from "../config/index.js";

async function signup(email, password, name) {
  // Check if user already exists
  const existing = await prisma.user.findUnique({ where: { email } });
  if (existing) {
    const error = new Error("Email already registered");
    error.status = 409;
    throw error;
  }

  // Hash password — NEVER store plain text
  const hashedPassword = await bcrypt.hash(password, 10);

  const user = await prisma.user.create({
    data: { email, password: hashedPassword, name },
  });

  const token = generateToken(user.id);
  return { user: { id: user.id, email: user.email, name: user.name }, token };
}

async function login(email, password) {
  const user = await prisma.user.findUnique({ where: { email } });
  if (!user) {
    const error = new Error("Invalid email or password");
    error.status = 401;
    throw error;
  }

  const validPassword = await bcrypt.compare(password, user.password);
  if (!validPassword) {
    const error = new Error("Invalid email or password");
    error.status = 401;
    throw error;
  }

  const token = generateToken(user.id);
  return { user: { id: user.id, email: user.email, name: user.name }, token };
}

async function getMe(userId) {
  const user = await prisma.user.findUnique({
    where: { id: userId },
    select: { id: true, email: true, name: true, createdAt: true },
  });

  if (!user) {
    const error = new Error("User not found");
    error.status = 404;
    throw error;
  }

  return user;
}

function generateToken(userId) {
  return jwt.sign({ userId }, config.jwtSecret, { expiresIn: "7d" });
}

export default { signup, login, getMe };
```

### File: `server/src/controllers/authController.js`

```js
import authService from "../services/authService.js";

async function signup(req, res, next) {
  try {
    const { email, password, name } = req.body;

    if (!email || !password || !name) {
      return res.status(400).json({ error: { message: "Email, password, and name are required" } });
    }
    if (password.length < 6) {
      return res.status(400).json({ error: { message: "Password must be at least 6 characters" } });
    }

    const result = await authService.signup(email, password, name);
    res.status(201).json(result);
  } catch (err) {
    next(err);
  }
}

async function login(req, res, next) {
  try {
    const { email, password } = req.body;

    if (!email || !password) {
      return res.status(400).json({ error: { message: "Email and password are required" } });
    }

    const result = await authService.login(email, password);
    res.json(result);
  } catch (err) {
    next(err);
  }
}

async function getMe(req, res, next) {
  try {
    const user = await authService.getMe(req.userId);
    res.json(user);
  } catch (err) {
    next(err);
  }
}

export default { signup, login, getMe };
```

### File: `server/src/routes/auth.js`

```js
import { Router } from "express";
import authController from "../controllers/authController.js";
import authenticate from "../middleware/auth.js";

const router = Router();

router.post("/signup", authController.signup);
router.post("/login",  authController.login);
router.get("/me",      authenticate, authController.getMe);

export default router;
```

### File: `server/src/middleware/auth.js`

**This is the gatekeeper.** Every protected route goes through here. No valid token = no access.

```js
import jwt from "jsonwebtoken";
import config from "../config/index.js";

function authenticate(req, res, next) {
  const header = req.headers.authorization;

  if (!header || !header.startsWith("Bearer ")) {
    return res.status(401).json({ error: { message: "Authentication required" } });
  }

  const token = header.split(" ")[1];

  try {
    const decoded = jwt.verify(token, config.jwtSecret);
    req.userId = decoded.userId;
    next();
  } catch (err) {
    return res.status(401).json({ error: { message: "Invalid or expired token" } });
  }
}

export default authenticate;
```

### Update: `server/src/config/index.js`

Add the JWT secret:

```js
import dotenv from "dotenv";
dotenv.config();

const config = {
  port: process.env.PORT || 3000,
  nodeEnv: process.env.NODE_ENV || "development",
  clientUrl: process.env.CLIENT_URL || "http://localhost:5173",
  jwtSecret: process.env.JWT_SECRET || "dev-secret-change-in-production",
};

export default config;
```

### Update: `server/.env`

Add:
```
JWT_SECRET=my-super-secret-key-change-this
```

### Update: `server/src/routes/index.js` — wire up auth + protect expenses

Replace the entire file:

```js
import { Router } from "express";
import expenseRoutes from "./expenses.js";
import authRoutes from "./auth.js";
import authenticate from "../middleware/auth.js";

const router = Router();

router.get("/health", (req, res) => {
  res.json({ status: "ok", timestamp: new Date().toISOString() });
});

// Auth routes (public)
router.use("/auth", authRoutes);

// Expense routes (protected — requires valid JWT)
router.use("/expenses", authenticate, expenseRoutes);

export default router;
```

### Now the frontend — `client/src/context/AuthContext.jsx`

```jsx
import { createContext, useContext, useState, useEffect } from "react";
import { login as apiLogin, signup as apiSignup, getMe } from "../api/auth";

const AuthContext = createContext();

export function AuthProvider({ children }) {
  const [user, setUser] = useState(null);
  const [loading, setLoading] = useState(true);

  // On app load, check if we have a stored token
  useEffect(() => {
    async function checkAuth() {
      const token = localStorage.getItem("token");
      if (token) {
        try {
          const userData = await getMe();
          setUser(userData);
        } catch {
          // Token is invalid/expired — clear it
          localStorage.removeItem("token");
        }
      }
      setLoading(false);
    }
    checkAuth();
  }, []);

  async function login(email, password) {
    const { user, token } = await apiLogin(email, password);
    localStorage.setItem("token", token);
    setUser(user);
  }

  async function signup(email, password, name) {
    const { user, token } = await apiSignup(email, password, name);
    localStorage.setItem("token", token);
    setUser(user);
  }

  function logout() {
    localStorage.removeItem("token");
    setUser(null);
  }

  return (
    <AuthContext.Provider value={{ user, loading, login, signup, logout, isAuthenticated: !!user }}>
      {children}
    </AuthContext.Provider>
  );
}

export function useAuth() {
  const context = useContext(AuthContext);
  if (!context) throw new Error("useAuth must be used within AuthProvider");
  return context;
}
```

### File: `client/src/components/ProtectedRoute.jsx`

```jsx
import { Navigate } from "react-router-dom";
import { useAuth } from "../context/AuthContext";

export default function ProtectedRoute({ children }) {
  const { isAuthenticated, loading } = useAuth();

  if (loading) return <div className="loading">Loading...</div>;
  if (!isAuthenticated) return <Navigate to="/login" replace />;

  return children;
}
```

### File: `client/src/pages/LoginPage.jsx` (replace placeholder)

```jsx
import { useState } from "react";
import { useNavigate, Link } from "react-router-dom";
import { useAuth } from "../context/AuthContext";

export default function LoginPage() {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [error, setError] = useState("");
  const { login } = useAuth();
  const navigate = useNavigate();

  async function handleSubmit(e) {
    e.preventDefault();
    setError("");
    try {
      await login(email, password);
      navigate("/expenses");
    } catch (err) {
      setError(err.message);
    }
  }

  return (
    <form onSubmit={handleSubmit} className="auth-form">
      <h1>Login</h1>
      {error && <div className="error">{error}</div>}
      <div className="form-group">
        <label>Email</label>
        <input type="email" value={email} onChange={(e) => setEmail(e.target.value)} required />
      </div>
      <div className="form-group">
        <label>Password</label>
        <input type="password" value={password} onChange={(e) => setPassword(e.target.value)} required />
      </div>
      <button type="submit" className="btn btn-primary" style={{ width: "100%" }}>Login</button>
      <p style={{ marginTop: "1rem", textAlign: "center" }}>
        Don't have an account? <Link to="/signup">Sign up</Link>
      </p>
    </form>
  );
}
```

### File: `client/src/pages/SignupPage.jsx` (replace placeholder)

```jsx
import { useState } from "react";
import { useNavigate, Link } from "react-router-dom";
import { useAuth } from "../context/AuthContext";

export default function SignupPage() {
  const [name, setName] = useState("");
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [error, setError] = useState("");
  const { signup } = useAuth();
  const navigate = useNavigate();

  async function handleSubmit(e) {
    e.preventDefault();
    setError("");
    if (password.length < 6) {
      setError("Password must be at least 6 characters");
      return;
    }
    try {
      await signup(email, password, name);
      navigate("/expenses");
    } catch (err) {
      setError(err.message);
    }
  }

  return (
    <form onSubmit={handleSubmit} className="auth-form">
      <h1>Sign Up</h1>
      {error && <div className="error">{error}</div>}
      <div className="form-group">
        <label>Name</label>
        <input type="text" value={name} onChange={(e) => setName(e.target.value)} required />
      </div>
      <div className="form-group">
        <label>Email</label>
        <input type="email" value={email} onChange={(e) => setEmail(e.target.value)} required />
      </div>
      <div className="form-group">
        <label>Password</label>
        <input type="password" value={password} onChange={(e) => setPassword(e.target.value)} required />
      </div>
      <button type="submit" className="btn btn-primary" style={{ width: "100%" }}>Sign Up</button>
      <p style={{ marginTop: "1rem", textAlign: "center" }}>
        Already have an account? <Link to="/login">Login</Link>
      </p>
    </form>
  );
}
```

### Update: `client/src/components/Layout.jsx` — auth-aware nav

```jsx
import { Link, Outlet } from "react-router-dom";
import { useAuth } from "../context/AuthContext";

export default function Layout() {
  const { isAuthenticated, user, logout } = useAuth();

  return (
    <div className="app">
      <nav className="navbar">
        <Link to="/" className="nav-brand">💰 Expense Tracker</Link>
        <div className="nav-links">
          {isAuthenticated ? (
            <>
              <Link to="/expenses">Expenses</Link>
              <Link to="/dashboard">Dashboard</Link>
              <span style={{ color: "#ccc" }}>Hi, {user?.name}</span>
              <button onClick={logout} className="btn" style={{ padding: "0.25rem 0.75rem" }}>
                Logout
              </button>
            </>
          ) : (
            <>
              <Link to="/login">Login</Link>
              <Link to="/signup">Sign Up</Link>
            </>
          )}
        </div>
      </nav>
      <main className="container">
        <Outlet />
      </main>
    </div>
  );
}
```

### Update: `client/src/App.jsx` — wrap with AuthProvider + protect routes

```jsx
import { BrowserRouter, Routes, Route } from "react-router-dom";
import { AuthProvider } from "./context/AuthContext";
import Layout from "./components/Layout";
import ProtectedRoute from "./components/ProtectedRoute";
import HomePage from "./pages/HomePage";
import ExpensesPage from "./pages/ExpensesPage";
import DashboardPage from "./pages/DashboardPage";
import LoginPage from "./pages/LoginPage";
import SignupPage from "./pages/SignupPage";

export default function App() {
  return (
    <BrowserRouter>
      <AuthProvider>
        <Routes>
          <Route path="/" element={<Layout />}>
            <Route index element={<HomePage />} />
            <Route path="expenses" element={<ProtectedRoute><ExpensesPage /></ProtectedRoute>} />
            <Route path="dashboard" element={<ProtectedRoute><DashboardPage /></ProtectedRoute>} />
            <Route path="login" element={<LoginPage />} />
            <Route path="signup" element={<SignupPage />} />
          </Route>
        </Routes>
      </AuthProvider>
    </BrowserRouter>
  );
}
```

### Verify
```bash
# Test auth endpoints:
curl -X POST http://localhost:3000/api/auth/signup \
  -H "Content-Type: application/json" \
  -d '{"email":"new@test.com","password":"123456","name":"New User"}'

# Copy the token from the response, then:
curl http://localhost:3000/api/expenses \
  -H "Authorization: Bearer YOUR_TOKEN_HERE"

# Without token — should return 401:
curl http://localhost:3000/api/expenses

# In the browser: signup, login, add expenses, check dashboard
```

### Commit
```bash
git add .
git commit -m "feat: JWT authentication, protected routes, login/signup UI"
```

---

## Phase 7: Testing (Day 11–12)

### Terminal Commands — Backend
```bash
cd server
npm install --save-dev jest @jest/globals supertest
```

### File: `server/jest.config.js`

```js
export default {
  transform: {},
  testEnvironment: "node",
};
```

### File: `server/tests/setup.js`

**Test helpers** — creates a test user and generates a token to use in tests.

```js
import prisma from "../src/lib/prisma.js";
import bcrypt from "bcryptjs";
import jwt from "jsonwebtoken";
import config from "../src/config/index.js";

export async function cleanDatabase() {
  await prisma.expense.deleteMany();
  await prisma.user.deleteMany();
}

export async function createTestUser() {
  const hashedPassword = await bcrypt.hash("password123", 10);
  const user = await prisma.user.create({
    data: { email: "test@test.com", password: hashedPassword, name: "Test User" },
  });
  const token = jwt.sign({ userId: user.id }, config.jwtSecret, { expiresIn: "1h" });
  return { user, token };
}

export async function disconnectDb() {
  await prisma.$disconnect();
}
```

### File: `server/tests/expenses.test.js`

```js
import { describe, it, expect, beforeAll, afterAll } from "@jest/globals";
import request from "supertest";
import app from "../src/app.js";
import { cleanDatabase, createTestUser, disconnectDb } from "./setup.js";

let token;
let userId;

beforeAll(async () => {
  await cleanDatabase();
  const testUser = await createTestUser();
  token = testUser.token;
  userId = testUser.user.id;
});

afterAll(async () => {
  await cleanDatabase();
  await disconnectDb();
});

describe("POST /api/expenses", () => {
  it("creates an expense with valid data", async () => {
    const res = await request(app)
      .post("/api/expenses")
      .set("Authorization", `Bearer ${token}`)
      .send({ amount: 25.50, category: "FOOD", description: "Lunch", date: "2026-04-11" });

    expect(res.status).toBe(201);
    expect(res.body.amount).toBe("25.5");
    expect(res.body.category).toBe("FOOD");
  });

  it("returns 400 for negative amount", async () => {
    const res = await request(app)
      .post("/api/expenses")
      .set("Authorization", `Bearer ${token}`)
      .send({ amount: -5, category: "FOOD", description: "Bad", date: "2026-04-11" });

    expect(res.status).toBe(400);
  });

  it("returns 400 for invalid category", async () => {
    const res = await request(app)
      .post("/api/expenses")
      .set("Authorization", `Bearer ${token}`)
      .send({ amount: 10, category: "INVALID", description: "Bad", date: "2026-04-11" });

    expect(res.status).toBe(400);
  });

  it("returns 401 without a token", async () => {
    const res = await request(app)
      .post("/api/expenses")
      .send({ amount: 10, category: "FOOD", description: "No auth", date: "2026-04-11" });

    expect(res.status).toBe(401);
  });
});

describe("GET /api/expenses", () => {
  it("returns expenses for the authenticated user", async () => {
    const res = await request(app)
      .get("/api/expenses")
      .set("Authorization", `Bearer ${token}`);

    expect(res.status).toBe(200);
    expect(Array.isArray(res.body.expenses)).toBe(true);
    expect(res.body.pagination).toBeDefined();
  });

  it("filters by category", async () => {
    const res = await request(app)
      .get("/api/expenses?category=FOOD")
      .set("Authorization", `Bearer ${token}`);

    expect(res.status).toBe(200);
    res.body.expenses.forEach((exp) => {
      expect(exp.category).toBe("FOOD");
    });
  });
});

describe("DELETE /api/expenses/:id", () => {
  it("deletes own expense", async () => {
    // Create one first
    const created = await request(app)
      .post("/api/expenses")
      .set("Authorization", `Bearer ${token}`)
      .send({ amount: 5, category: "OTHER", description: "To delete", date: "2026-04-11" });

    const res = await request(app)
      .delete(`/api/expenses/${created.body.id}`)
      .set("Authorization", `Bearer ${token}`);

    expect(res.status).toBe(204);
  });
});
```

### File: `server/tests/auth.test.js`

```js
import { describe, it, expect, beforeAll, afterAll } from "@jest/globals";
import request from "supertest";
import app from "../src/app.js";
import { cleanDatabase, disconnectDb } from "./setup.js";

beforeAll(async () => {
  await cleanDatabase();
});

afterAll(async () => {
  await cleanDatabase();
  await disconnectDb();
});

describe("POST /api/auth/signup", () => {
  it("creates a new user and returns token", async () => {
    const res = await request(app)
      .post("/api/auth/signup")
      .send({ email: "new@test.com", password: "password123", name: "New" });

    expect(res.status).toBe(201);
    expect(res.body.token).toBeDefined();
    expect(res.body.user.email).toBe("new@test.com");
  });

  it("rejects duplicate email", async () => {
    const res = await request(app)
      .post("/api/auth/signup")
      .send({ email: "new@test.com", password: "password123", name: "Dupe" });

    expect(res.status).toBe(409);
  });

  it("rejects short password", async () => {
    const res = await request(app)
      .post("/api/auth/signup")
      .send({ email: "short@test.com", password: "123", name: "Short" });

    expect(res.status).toBe(400);
  });
});

describe("POST /api/auth/login", () => {
  it("returns token for valid credentials", async () => {
    const res = await request(app)
      .post("/api/auth/login")
      .send({ email: "new@test.com", password: "password123" });

    expect(res.status).toBe(200);
    expect(res.body.token).toBeDefined();
  });

  it("rejects wrong password", async () => {
    const res = await request(app)
      .post("/api/auth/login")
      .send({ email: "new@test.com", password: "wrongpassword" });

    expect(res.status).toBe(401);
  });
});
```

### Update: `server/package.json` — add test script:
```json
{
  "scripts": {
    "dev": "node --watch src/server.js",
    "start": "node src/server.js",
    "test": "node --experimental-vm-modules node_modules/.bin/jest --runInBand --forceExit"
  }
}
```

### Terminal Commands — Frontend
```bash
cd client
npm install --save-dev vitest jsdom @testing-library/react @testing-library/jest-dom @testing-library/user-event
```

### File: `client/vitest.config.js`

```js
import { defineConfig } from "vitest/config";
import react from "@vitejs/plugin-react";

export default defineConfig({
  plugins: [react()],
  test: {
    environment: "jsdom",
    setupFiles: "./src/test/setup.js",
  },
});
```

### File: `client/src/test/setup.js`

```js
import "@testing-library/jest-dom";
```

### File: `client/src/components/ExpenseCard.test.jsx`

```jsx
import { describe, it, expect, vi } from "vitest";
import { render, screen } from "@testing-library/react";
import userEvent from "@testing-library/user-event";
import ExpenseCard from "./ExpenseCard";

const mockExpense = {
  id: 1,
  amount: "25.50",
  category: "FOOD",
  description: "Lunch at cafe",
  date: "2026-04-11T00:00:00.000Z",
};

describe("ExpenseCard", () => {
  it("renders expense details", () => {
    render(<ExpenseCard expense={mockExpense} onEdit={() => {}} onDelete={() => {}} />);

    expect(screen.getByText("Lunch at cafe")).toBeInTheDocument();
    expect(screen.getByText("FOOD")).toBeInTheDocument();
    expect(screen.getByText("$25.50")).toBeInTheDocument();
  });

  it("calls onDelete when delete button clicked", async () => {
    const onDelete = vi.fn();
    render(<ExpenseCard expense={mockExpense} onEdit={() => {}} onDelete={onDelete} />);

    await userEvent.click(screen.getByText("Delete"));
    expect(onDelete).toHaveBeenCalledWith(1);
  });

  it("calls onEdit when edit button clicked", async () => {
    const onEdit = vi.fn();
    render(<ExpenseCard expense={mockExpense} onEdit={onEdit} onDelete={() => {}} />);

    await userEvent.click(screen.getByText("Edit"));
    expect(onEdit).toHaveBeenCalledWith(mockExpense);
  });
});
```

### File: `client/src/components/ExpenseList.test.jsx`

```jsx
import { describe, it, expect } from "vitest";
import { render, screen } from "@testing-library/react";
import ExpenseList from "./ExpenseList";

describe("ExpenseList", () => {
  it("shows loading state", () => {
    render(<ExpenseList expenses={[]} loading={true} error={null} onEdit={() => {}} onDelete={() => {}} />);
    expect(screen.getByText("Loading expenses...")).toBeInTheDocument();
  });

  it("shows error message", () => {
    render(<ExpenseList expenses={[]} loading={false} error="Something broke" onEdit={() => {}} onDelete={() => {}} />);
    expect(screen.getByText("Something broke")).toBeInTheDocument();
  });

  it("shows empty state", () => {
    render(<ExpenseList expenses={[]} loading={false} error={null} onEdit={() => {}} onDelete={() => {}} />);
    expect(screen.getByText("No expenses yet. Add one!")).toBeInTheDocument();
  });
});
```

### Update: `client/package.json` — add test script:
```json
{
  "scripts": {
    "dev": "vite",
    "build": "vite build",
    "preview": "vite preview",
    "test": "vitest run",
    "test:watch": "vitest"
  }
}
```

### Verify
```bash
cd server && npm test
cd ../client && npm test
```

### Commit
```bash
git add .
git commit -m "feat: backend + frontend tests (Jest, Supertest, Vitest, RTL)"
```

---

## Phase 8: Docker (Day 13)

### File: `docker/server.Dockerfile`

```dockerfile
# Stage 1: Build
FROM node:20-alpine AS builder
WORKDIR /app
COPY server/package*.json ./
RUN npm ci
COPY server/ .
RUN npx prisma generate

# Stage 2: Runtime (smaller image)
FROM node:20-alpine
WORKDIR /app

# Run as non-root user for security
RUN addgroup -S appgroup && adduser -S appuser -G appgroup

COPY --from=builder /app .

USER appuser

EXPOSE 3000

CMD ["node", "src/server.js"]
```

### File: `docker/client.Dockerfile`

```dockerfile
# Stage 1: Build the React app
FROM node:20-alpine AS builder
WORKDIR /app
COPY client/package*.json ./
RUN npm ci
COPY client/ .
ARG VITE_API_URL
ENV VITE_API_URL=$VITE_API_URL
RUN npm run build

# Stage 2: Serve with Nginx
FROM nginx:alpine
COPY --from=builder /app/dist /usr/share/nginx/html
COPY docker/nginx.conf /etc/nginx/conf.d/default.conf

EXPOSE 80
```

### File: `docker/nginx.conf`

**Why Nginx?** It serves static files 10x faster than Node.js, handles compression, and proxies API requests to the backend — solving CORS in production.

```nginx
server {
    listen 80;

    # Serve React static files
    location / {
        root /usr/share/nginx/html;
        index index.html;
        try_files $uri $uri/ /index.html;  # React Router — all routes go to index.html
    }

    # Proxy API requests to the backend container
    location /api/ {
        proxy_pass http://server:3000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    }
}
```

### Update: `docker-compose.yml` (project root — full stack)

```yaml
services:
  postgres:
    image: postgres:16-alpine
    container_name: expense-tracker-db
    environment:
      POSTGRES_USER: expense_user
      POSTGRES_PASSWORD: expense_pass
      POSTGRES_DB: expense_tracker
    ports:
      - "5432:5432"
    volumes:
      - pgdata:/var/lib/postgresql/data
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U expense_user -d expense_tracker"]
      interval: 5s
      timeout: 5s
      retries: 5

  server:
    build:
      context: .
      dockerfile: docker/server.Dockerfile
    container_name: expense-tracker-api
    environment:
      DATABASE_URL: postgresql://expense_user:expense_pass@postgres:5432/expense_tracker
      JWT_SECRET: docker-secret-change-in-prod
      NODE_ENV: production
      CLIENT_URL: http://localhost
      PORT: 3000
    ports:
      - "3000:3000"
    depends_on:
      postgres:
        condition: service_healthy
    command: >
      sh -c "npx prisma migrate deploy && node src/server.js"

  client:
    build:
      context: .
      dockerfile: docker/client.Dockerfile
      args:
        VITE_API_URL: /api
    container_name: expense-tracker-client
    ports:
      - "80:80"
    depends_on:
      - server

volumes:
  pgdata:
```

### File: `Makefile`

```makefile
.PHONY: dev build down logs

dev:
	docker compose up -d postgres
	@echo "PostgreSQL running. Start server & client manually for dev."

build:
	docker compose up --build

down:
	docker compose down

logs:
	docker compose logs -f
```

### Verify
```bash
# Build and run everything
docker compose up --build

# Visit http://localhost — full app should work
# Signup, login, add expenses, check dashboard
```

### Commit
```bash
git add .
git commit -m "feat: Docker multi-stage builds, Docker Compose full stack, Nginx proxy"
```

---

## Phase 9: CI/CD Pipeline (Day 14)

### Terminal Commands
```bash
cd server && npm install --save-dev eslint
cd ../client && npm install --save-dev eslint
```

### File: `.github/workflows/ci.yml`

```yaml
name: CI/CD Pipeline

on:
  push:
    branches: [main]
  pull_request:
    branches: [main]

jobs:
  lint:
    name: Lint
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with:
          node-version: 20
      - name: Lint server
        run: |
          cd server
          npm ci
          npx eslint src/ --no-eslintrc --rule '{"no-unused-vars": "warn"}' || true
      - name: Lint client
        run: |
          cd client
          npm ci
          npx eslint src/ --no-eslintrc --rule '{"no-unused-vars": "warn"}' || true

  test-backend:
    name: Backend Tests
    needs: lint
    runs-on: ubuntu-latest
    services:
      postgres:
        image: postgres:16-alpine
        env:
          POSTGRES_USER: test_user
          POSTGRES_PASSWORD: test_pass
          POSTGRES_DB: test_db
        ports:
          - 5432:5432
        options: >-
          --health-cmd="pg_isready -U test_user -d test_db"
          --health-interval=5s
          --health-timeout=5s
          --health-retries=5
    env:
      DATABASE_URL: postgresql://test_user:test_pass@localhost:5432/test_db
      JWT_SECRET: test-secret
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with:
          node-version: 20
      - name: Install & test
        run: |
          cd server
          npm ci
          npx prisma migrate deploy
          npm test

  test-frontend:
    name: Frontend Tests
    needs: lint
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with:
          node-version: 20
      - name: Install & test
        run: |
          cd client
          npm ci
          npm test

  build:
    name: Build Docker Images
    needs: [test-backend, test-frontend]
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Build server image
        run: docker build -f docker/server.Dockerfile -t expense-tracker-server .
      - name: Build client image
        run: docker build -f docker/client.Dockerfile --build-arg VITE_API_URL=/api -t expense-tracker-client .

  # Uncomment and configure when you have Render set up:
  # deploy:
  #   name: Deploy to Render
  #   needs: build
  #   if: github.ref == 'refs/heads/main' && github.event_name == 'push'
  #   runs-on: ubuntu-latest
  #   steps:
  #     - name: Deploy Backend
  #       run: |
  #         curl -X POST "https://api.render.com/deploy/srv-${{ secrets.RENDER_BACKEND_ID }}?key=${{ secrets.RENDER_API_KEY }}"
  #     - name: Deploy Frontend
  #       run: |
  #         curl -X POST "https://api.render.com/deploy/srv-${{ secrets.RENDER_FRONTEND_ID }}?key=${{ secrets.RENDER_API_KEY }}"
```

### Verify
```bash
git add .
git commit -m "feat: GitHub Actions CI pipeline (lint, test, build)"
git push origin main
# Go to your GitHub repo → Actions tab — watch the pipeline run
```

---

## Phase 10: Deploy to Render (Day 15)

This phase is configuration, not code. Here are the exact steps:

### Step 1: Create PostgreSQL on Render
1. Go to render.com → Dashboard → New → PostgreSQL
2. Name: `expense-tracker-db`
3. Choose Free tier
4. Create → Copy the **External Database URL** (starts with `postgresql://`)

### Step 2: Deploy Backend
1. New → Web Service → Connect your GitHub repo
2. **Root Directory:** `server`
3. **Build Command:** `npm install && npx prisma generate && npx prisma migrate deploy`
4. **Start Command:** `node src/server.js`
5. **Environment Variables:**
   - `DATABASE_URL` = (paste the External Database URL from Step 1)
   - `JWT_SECRET` = (generate a random string: `openssl rand -hex 32`)
   - `NODE_ENV` = `production`
   - `CLIENT_URL` = (you'll update this after deploying frontend)
6. Deploy → Note the backend URL (e.g. `https://expense-tracker-api-xxxx.onrender.com`)

### Step 3: Deploy Frontend
1. New → Static Site → Connect same repo
2. **Root Directory:** `client`
3. **Build Command:** `npm install && npm run build`
4. **Publish Directory:** `dist`
5. **Environment Variables:**
   - `VITE_API_URL` = `https://expense-tracker-api-xxxx.onrender.com/api` (your backend URL + `/api`)
6. **Rewrite Rule:** Add redirect — Source: `/*`, Destination: `/index.html`, Action: `Rewrite`
7. Deploy → Note the frontend URL

### Step 4: Update Backend CORS
Go back to the backend service on Render → Environment → Update:
- `CLIENT_URL` = your frontend's Render URL (e.g. `https://expense-tracker-xxxx.onrender.com`)

### Step 5: Verify
1. Visit your frontend URL
2. Sign up with a new account
3. Add a few expenses
4. Check the dashboard
5. Log out and log back in — data persists

### Step 6: Update README

Add at the top of your `README.md`:
```markdown
# Expense Tracker

**Live Demo:** [your-frontend-url.onrender.com](https://your-frontend-url.onrender.com)

Full-stack expense tracking application built from scratch.

## Tech Stack
- **Frontend:** React, Vite, React Router
- **Backend:** Express.js, Prisma, PostgreSQL
- **Auth:** JWT
- **Testing:** Jest, Supertest, Vitest, React Testing Library
- **DevOps:** Docker, Docker Compose, GitHub Actions, Render

## Architecture
```
Browser → React (Render Static Site)
              ↓ fetch /api/*
         Express API (Render Web Service)
              ↓ Prisma ORM
         PostgreSQL (Render Database)
```
```

### Final Commit
```bash
git add .
git commit -m "docs: deployment config, live demo link"
git push origin main
```

---

## Verification Checklist

| Phase | How to verify |
|---|---|
| 0 | Repo exists on GitHub with clean structure |
| 1 | `curl localhost:3000/api/health` → `{"status":"ok"}` |
| 2 | `npx prisma studio` shows tables with seed data |
| 3 | All 6 endpoints work via curl/Postman |
| 4 | React loads at `localhost:5173`, nav works |
| 5 | Full CRUD in UI works, dashboard shows stats |
| 6 | Signup → login → only own expenses visible → 401 without token |
| 7 | `npm test` green in both server/ and client/ |
| 8 | `docker compose up --build` → full app at `localhost` |
| 9 | GitHub Actions pipeline runs green on push |
| 10 | Live URL: signup → expenses → dashboard → works |

---

## What to Add Next (After Completing All 10 Phases)

- Rate limiting on auth endpoints
- File upload for receipt images
- Email notifications (welcome email, weekly summary)
- WebSocket for real-time dashboard updates
- Admin panel
- Cursor-based pagination
- HttpOnly cookie auth (replace localStorage)
- Monitoring with health dashboards
