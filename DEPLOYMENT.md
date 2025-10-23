# 🚀 Deployment Guide

Complete guide to deploy Sure Financial to GitHub, Vercel (frontend), and Render (backend).

---

## 📋 Prerequisites

- Git installed on your system
- GitHub account
- Vercel account (free tier available)
- Render account (free tier available)
- Backend and frontend code ready in `d:\sure_financial`

---

## Step 1: Push Code to GitHub

### 1.1 Initialize Git Repository

```powershell
# Navigate to project root
cd d:\sure_financial

# Initialize Git (if not already done)
git init

# Add remote repository
git remote add origin https://github.com/Shobit04/sure_financial.git
```

### 1.2 Stage and Commit Files

```powershell
# Stage all files
git add .

# Commit changes
git commit -m "Initial commit: FastAPI backend + Next.js frontend with 6 bank parsers"
```

### 1.3 Push to GitHub

```powershell
# Push to main branch
git push -u origin main

# If above fails, try force push (first time only)
git push -u origin main --force
```

---

## Step 2: Deploy Backend to Render

### 2.1 Create New Web Service

1. Go to [Render Dashboard](https://dashboard.render.com/)
2. Click **New** → **Web Service**
3. Connect your GitHub account (if not already connected)
4. Select repository: `Shobit04/sure_financial`

### 2.2 Configure Backend Settings

| Setting | Value |
|---------|-------|
| **Name** | `sure-financial-backend` |
| **Region** | Choose closest to your location |
| **Root Directory** | `backend` |
| **Environment** | `Python 3` |
| **Build Command** | `pip install -r requirements.txt` |
| **Start Command** | `uvicorn main:app --host 0.0.0.0 --port $PORT` |

### 2.3 Environment Variables (Optional)

**No environment variables needed** — Supabase has been fully removed.

If you want to add OCR support in production:
- **Key**: `TESSERACT_CMD`
- **Value**: `/usr/bin/tesseract` (default Linux path)

### 2.4 Deploy Backend

1. Click **Create Web Service**
2. Wait for deployment to complete (5-10 minutes)
3. Copy your backend URL: `https://sure-financial-backend.onrender.com`

**Important**: Render free tier sleeps after 15 minutes of inactivity. First request after sleep takes 30-60 seconds.

---

## Step 3: Deploy Frontend to Vercel

### 3.1 Create New Project

1. Go to [Vercel Dashboard](https://vercel.com/dashboard)
2. Click **Add New** → **Project**
3. Import Git Repository: `Shobit04/sure_financial`

### 3.2 Configure Frontend Settings

| Setting | Value |
|---------|-------|
| **Framework Preset** | Next.js |
| **Root Directory** | `frontend` |
| **Build Command** | `npm run build` (auto-detected) |
| **Output Directory** | `.next` (auto-detected) |
| **Install Command** | `npm install` (auto-detected) |

### 3.3 Add Environment Variable

**Critical**: Add this environment variable to connect frontend to backend.

1. In **Environment Variables** section:
   - **Key**: `NEXT_PUBLIC_API_URL`
   - **Value**: `https://sure-financial-backend.onrender.com` (your Render backend URL)
   - **Apply to**: All environments (Production, Preview, Development)

2. Click **Add**

### 3.4 Deploy Frontend

1. Click **Deploy**
2. Wait for deployment to complete (2-5 minutes)
3. Your app will be live at: `https://your-app.vercel.app`

**Vercel will auto-generate a domain**. You can customize it in Project Settings → Domains.

---

## Step 4: Verify Deployment

### 4.1 Test Backend API

```powershell
# Check backend health
curl https://sure-financial-backend.onrender.com/docs

# Test extraction endpoint
curl -X POST https://sure-financial-backend.onrender.com/extract \
  -F "file=@test_statement.pdf"
```

### 4.2 Test Frontend

1. Open your Vercel URL in browser: `https://your-app.vercel.app`
2. Navigate to Upload page
3. Upload a test PDF statement
4. Verify extraction results display correctly

### 4.3 Test API Connection

Check browser console (F12) for errors:
- ✅ **Success**: `POST https://sure-financial-backend.onrender.com/extract 200`
- ❌ **Failure**: `CORS error` or `Network error`

If CORS error occurs, check `backend/main.py` CORS configuration:
```python
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Change to specific domain in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
```

---

## Step 5: Optional Configurations

### 5.1 Custom Domain (Vercel)

1. Go to Project Settings → Domains
2. Add your custom domain
3. Configure DNS settings as instructed by Vercel

### 5.2 Environment Variables (Add Later)

If you add Tesseract OCR or database:

**Render Backend**:
- `TESSERACT_CMD` → `/usr/bin/tesseract`
- `DATABASE_URL` → (if you add database)

**Vercel Frontend**:
- `NEXT_PUBLIC_API_URL` → Already added

### 5.3 Render Auto-Deploy

Render automatically deploys when you push to `main` branch on GitHub.

To disable:
- Go to Render dashboard → Settings → Auto-Deploy → Off

### 5.4 Vercel Auto-Deploy

Vercel automatically deploys on every push to any branch.

To disable:
- Go to Vercel dashboard → Settings → Git → Ignored Build Step

---

## 🔧 Troubleshooting

### Backend Issues

**Deployment fails on Render**:
- Check build logs for errors
- Verify `requirements.txt` has all dependencies
- Ensure Python version is compatible (3.10+)

**Backend responds with 500 errors**:
- Check Render logs: Dashboard → Logs
- Verify file paths (use relative paths)
- Check for missing dependencies

**Backend is slow (first request)**:
- Normal for Render free tier (sleeps after 15min)
- Consider upgrading to paid tier or keeping alive with cron job

### Frontend Issues

**Build fails on Vercel**:
- Check build logs for errors
- Verify `package.json` has all dependencies
- Check Node version compatibility (18+)

**API calls fail with CORS error**:
- Add Vercel domain to CORS in `backend/main.py`
- Restart Render service after updating CORS

**Environment variable not working**:
- Redeploy after adding environment variable
- Check variable name: must start with `NEXT_PUBLIC_` for client-side access

### Connection Issues

**Frontend can't reach backend**:
- Verify `NEXT_PUBLIC_API_URL` is correct
- Check backend is running: visit `/docs` endpoint
- Inspect Network tab in browser console

**CORS errors**:
Update `backend/main.py`:
```python
allow_origins=[
    "http://localhost:3000",
    "https://your-app.vercel.app",
    "https://your-custom-domain.com"
]
```

---

## 📊 Deployment Checklist

- [ ] Code pushed to GitHub
- [ ] `.gitignore` file created (excludes .venv, node_modules, .env)
- [ ] Backend deployed to Render
- [ ] Backend URL copied
- [ ] Frontend deployed to Vercel
- [ ] Environment variable `NEXT_PUBLIC_API_URL` added to Vercel
- [ ] Backend API tested (`/docs` endpoint)
- [ ] Frontend tested (upload page)
- [ ] API connection verified (upload PDF and check extraction)
- [ ] README updated with live URLs

---

## 🎯 Post-Deployment

### Update README

Add live URLs to main README:

```markdown
## 🚀 Live Demo

- **Frontend**: https://your-app.vercel.app
- **Backend API**: https://sure-financial-backend.onrender.com
- **API Docs**: https://sure-financial-backend.onrender.com/docs
```

### Share Your Project

- GitHub: https://github.com/Shobit04/sure_financial
- Live App: https://your-app.vercel.app
- LinkedIn: Share your deployment!

---

## 💡 Tips

1. **Render Free Tier**: Sleeps after 15min inactivity. First request takes ~60s.
2. **Vercel Free Tier**: 100GB bandwidth/month. Plenty for personal projects.
3. **GitHub Actions**: Set up CI/CD for automated testing before deployment.
4. **Monitoring**: Use Render logs and Vercel analytics to monitor usage.
5. **Scaling**: Upgrade to paid tiers when traffic increases.

---

**🎉 Congratulations! Your app is now live!**

**Need help?** Check:
- Render docs: https://render.com/docs
- Vercel docs: https://vercel.com/docs
- GitHub Issues: Create an issue in your repo
