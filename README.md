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
| DB_HOST | Database host |
| DB_PORT | Database port |
| DB_NAME | Database name |
| DB_USER | Database user |
| DB_PASSWORD | Database password |
| JWT_SECRET | Secret key for JWT signing |
| JWT_EXPIRES_IN | JWT expiration time (seconds) |

### Optional Variables

| Variable | Description |
|--------|------------|
| LOG_LEVEL | Logging level (default: info) |
| EXTERNAL_API_URL | External service base URL |
| EXTERNAL_API_KEY | External service API key |

### Environment Files

- `.env.example` → reference template
- `.env.development` → local development
- `.env.staging` → staging environment
- `.env.production` → production environment

> Environment files are not committed to version control.
