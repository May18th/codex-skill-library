---
name: vue-django-mysql-fullstack
description: Use when creating, extending, or debugging a general-purpose full-stack web application that explicitly uses Vue 3 with Vite and Element Plus, Django REST Framework, and MySQL; not for unrelated stacks, one-off frontend-only work, or project-specific competition requirements.
---

# Vue + Django + MySQL Full-Stack Development

Use this workflow for ordinary learning, personal, or small-business applications. Keep the project domain generic unless the user supplies a concrete business requirement. The workflow is a development guide, not permission to overwrite an existing project, install system-wide software, expose a service, or deploy to production.

## 1. Establish scope before editing

1. Inspect the existing repository, its `AGENTS.md`, current branches, uncommitted changes, runtimes, and test commands. Preserve the existing architecture when it already satisfies the request.
2. Record the requested users, business entities, pages, roles, important workflows, constraints, and acceptance checks. The article/content-management example below is a teaching example, not a default requirement.
3. Ask only for missing decisions that materially change the schema, permissions, or user workflow. Otherwise state conservative assumptions and proceed.
4. For a new project, verify supported Python, Django, Node, and MySQL versions against their official release/support documentation at implementation time. If the user pins an unsupported or end-of-life version, explain the risk and ask before changing that constraint.
5. Turn acceptance criteria into observable checks before implementation. For behavior changes, follow the repository's test-first convention; run relevant tests before and after.

## 2. Keep a clear project boundary

For a new project, use a simple layout such as:

```text
project-name/
  backend/
    config/                 # Django settings and URL configuration
    apps/<domain-app>/      # domain models, serializers, views, URLs, tests
    static/
    templates/
    requirements.txt
    .env.example
  frontend/
    src/
      api/
      components/
      router/
      views/
    package.json
  database/
    init.sql
  docs/
    setup.md
  .gitignore
```

Keep local virtual environments, `node_modules`, build output, `.env`, database dumps, and credentials out of version control. The user may choose another layout if the repository already has conventions.

## 3. Configure the backend and database

1. Create and activate a project-local Python virtual environment. Install Django, Django REST Framework, a MySQL driver supported by the chosen Django version, and only necessary packages. Pin reproducible versions in `requirements.txt`.
2. Create the MySQL database and an application-specific database user with only the permissions needed by the application. Configure `utf8mb4` and a compatible collation. Never use the root account for the running application.
3. Keep `SECRET_KEY`, database password, allowed hosts, and other environment-specific values in environment variables. Commit only placeholder names and safe example values in `.env.example`; never print or commit real credentials.
4. Configure Django's database connection, Chinese locale where relevant, explicit timezone, static/template paths, and environment-specific `DEBUG`/`ALLOWED_HOSTS` values.
5. Configure CORS with an explicit allowlist of development/production frontend origins. Do not use wildcard origins with credentials. CORS is not authentication or authorization.
6. Add the domain app and DRF. Choose authentication based on the actual client and deployment boundary. Do not assume a JWT package or token storage strategy without checking the requirement; protect cookie-based auth against CSRF and keep browser tokens out of unsafe persistent storage.
7. If the project needs a custom user model, define it before the first migration. Use Django's password hashing and authentication APIs; never store or compare plaintext passwords.

For the optional generic content example, an article can have `title`, `content`, an author relation, `created_at`, and `updated_at`. A user should normally use Django's user model and groups/permissions rather than a second plaintext-password table. Treat this as an example only.

## 4. Build a small, explicit REST API

1. Define model constraints and relationships before serializers and endpoints. Add indexes only for demonstrated query needs.
2. Use serializers for input validation and output shape. Keep business rules out of templates and avoid returning internal fields or secrets.
3. Use DRF views/viewsets and routers where they make the API clearer. Document methods, request fields, response fields, status codes, pagination, and authentication requirements.
4. Apply object-level and role permissions on the server for every protected read and write. Hiding a frontend button is not authorization. Prevent users from changing ownership or role fields through mass assignment.
5. Use suitable HTTP semantics: `GET` reads, `POST` creates/actions, `PUT` replaces, `PATCH` partially updates, and `DELETE` removes. Return validation errors with a stable, understandable structure.
6. Register models in Django admin only when an administrative data workflow is useful; constrain admin access to authorized staff accounts.
7. Write API tests for anonymous access, valid access, invalid input, ownership boundaries, role boundaries, and CRUD behavior. Use a disposable test database, not a user's production data.

## 5. Build the Vue client

1. Scaffold Vue 3 with Vite. Add Element Plus, Axios, and Vue Router only when required by the agreed pages and interactions.
2. Organize API calls under `src/api`, route-level pages under `src/views`, reusable UI under `src/components`, and route definitions under `src/router`.
3. Keep the API base URL in environment configuration, for example `VITE_API_BASE_URL`; frontend environment values are public and must never contain server secrets.
4. Centralize Axios base URL, timeouts, JSON handling, and error normalization. Add auth headers only for the chosen auth design. Handle expired sessions and authorization failures without retry loops or leaking tokens into logs.
5. Implement loading, empty, validation-error, server-error, and success states. Keep forms keyboard accessible and provide clear field-level validation.
6. Add responsive behavior for agreed desktop and mobile workflows. Do not rely on screenshots alone: test the actual forms, navigation, and API states.
7. For a content-management example, pages might include a public list/detail and an authorized management view. Do not generate user/role-management screens unless required; account management raises additional security and policy questions.

## 6. Integrate and verify end to end

1. Run database migrations against the intended local database and inspect migration output. Do not run destructive migration or reset commands against unknown or production data.
2. Start Django locally and verify the health/root route and API endpoints. Start Vite locally and verify the UI in a browser when browser tooling is available.
3. Exercise create, list, detail, update, and delete from the UI or API, then confirm expected persisted state in MySQL. Verify access control with at least one unauthorized request.
4. Test validation failures, empty results, backend unavailable, expired/invalid authentication, and small/mobile viewport behavior.
5. Run backend tests and frontend checks/build. Report exact commands and results; distinguish checks run from checks not run.
6. Check repository status and inspect the final diff for secrets, generated files, unexpected schema changes, and unrelated modifications.

## 7. Deliverables

When the user requests a runnable project, provide:

- Source code for the backend and frontend.
- `backend/requirements.txt` and `frontend/package.json` with necessary dependencies.
- A safe MySQL initialization script that creates the database/character set but contains no credentials or real user data.
- `.env.example` with variable names and placeholders only.
- A setup guide with prerequisites, database creation, environment configuration, migrations, admin creation if needed, and exact commands to start each server.
- API and permission notes plus verification results.

Do not claim the project is production-ready based only on local startup. Production deployment additionally requires explicit deployment scope and a separate review of secrets, HTTPS, allowed hosts, CORS/CSRF, backups, logging, dependency support, and operational monitoring.

## Common failure checks

- **Django starts but cannot connect to MySQL:** verify service status, host/port, database/user grants, driver, and environment values; do not paste passwords into logs.
- **Browser reports CORS errors:** compare the exact page origin with the configured allowlist; do not disable CORS globally.
- **API works in browser but permissions are wrong:** test server-side permissions directly with anonymous and alternate-user requests.
- **Frontend shows stale or malformed data:** inspect the network request, response schema, Axios normalization, and loading/error states before changing the database.
- **Migration unexpectedly drops or rewrites data:** stop; inspect migration SQL and database target before applying it.
