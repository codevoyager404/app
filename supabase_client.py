from supabase import create_client, Client

SUPABASE_URL = "https://your-project.supabase.co"
SUPABASE_KEY = "your-service-role-key"  # NEVER USE anon key in backend

supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)