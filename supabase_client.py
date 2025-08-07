from supabase import create_client, Client

SUPABASE_URL = "https://qqmindjleglhihsvdbmd.supabase.co"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InFxbWluZGpsZWdsaGloc3ZkYm1kIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NTQ1Nzg3MTIsImV4cCI6MjA3MDE1NDcxMn0.WBTXVEnWwSlyxcYHkCobE8i4axW2J0e20xAakZCVNk4"  # NEVER USE anon key in backend

supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)