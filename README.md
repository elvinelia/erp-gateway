# ERP Backend
Initialize FastAPI Project Structure

## Environment Variables

The application uses environment-based configuration.

### Required Variables

| Variable | Description |
|--------|------------|
| ENVIRONMENT | Application environment (`development`, `staging`, `production`) |
| APP_NAME | Application name |
| APP_PORT | Port where the application runs |
| DATABASE_URL | Database connection string |
| JWT_SECRET | Secret key for JWT signing |
| JWT_EXPIRES_IN | JWT expiration time (seconds) |

### Environment Files

- `.env.example` → reference template
- `.env.development` → local development
- `.env.staging` → staging environment
- `.env.production` → production environment

> Environment files are not committed to version control.
