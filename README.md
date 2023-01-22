# TodoWebApp

## A webapp project to create a personal todolist app with logins, auth. And implementing custom frontend, backend, and database.

Stack split into frontend, backend, and databse: 
1. astro+svelte for frontend served by Deno with ssr
2. Flask api backend for authentication and to connect frontend with database
3. MariaDB container for database

Then Containerize all three with docker and combine into one docker compose
