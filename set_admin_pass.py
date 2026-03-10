import asyncio
import os
from backend.database import connect_db, disconnect_db, prisma
from backend.auth import get_password_hash

async def main():
    os.environ["DATABASE_URL"] = "postgresql://neondb_owner:npg_iSw0hrW7cGDQ@ep-lively-river-ai2gtguu-pooler.c-4.us-east-1.aws.neon.tech/neondb?sslmode=require"
    await connect_db()
    
    existing_admin = await prisma.user.find_unique(where={'roll_number': "admin"})
    hashed = get_password_hash("password123")
    
    if not existing_admin:
         await prisma.user.create(data={
             'roll_number': "admin",
             'full_name': "System Admin",
             'password_hash': hashed,
             'role': "admin",
             'department': "admin"
         })
         print("Created admin user with password123")
    else:
         await prisma.user.update(where={'roll_number': "admin"}, data={'password_hash': hashed})
         print("Updated admin user password to password123")
         
    await disconnect_db()

if __name__ == '__main__':
    asyncio.run(main())
