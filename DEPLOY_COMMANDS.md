# 🚀 Quick Deployment Commands

All commands to deploy Sure Financial from local machine to production.

---

## 📦 Step 1: Push to GitHub

```powershell
# Navigate to project root
cd d:\sure_financial

# Initialize Git (if not already done)
git init

# Add all files
git add .

# Commit
git commit -m "Initial commit: FastAPI backend + Next.js frontend with 6 bank parsers"

# Add remote repository
git remote add origin https://github.com/Shobit04/sure_financial.git

# Push to main branch
git push -u origin main

# If push fails (first time), force push:
git push -u origin main --force
```

---

## 🔧 Step 2: Deploy Backend (Render)

### Via Render Dashboard:

1. Go to https://dashboard.render.com/
2. Click **New** → **Web Service**
3. Connect GitHub repo: `Shobit04/sure_financial`
4. Configure:
   ```
   Name: sure-financial-backend
   Root Directory: backend
   Environment: Python 3
   Build Command: pip install -r requirements.txt
   Start Command: uvicorn main:app --host 0.0.0.0 --port $PORT
   ```
5. Click **Create Web Service**
6. Copy backend URL: `https://sure-financial-backend.onrender.com`

---

## 🎨 Step 3: Deploy Frontend (Vercel)

### Via Vercel Dashboard:

1. Go to https://vercel.com/dashboard
2. Click **Add New** → **Project**
3. Import repo: `Shobit04/sure_financial`
4. Configure:
   ```
   Framework Preset: Next.js
   Root Directory: frontend
   Build Command: npm run build (auto-detected)
   Output Directory: .next (auto-detected)
   ```
5. Add Environment Variable:
   ```
   Key: NEXT_PUBLIC_API_URL
   Value: https://sure-financial-backend.onrender.com
   ```
6. Click **Deploy**
7. Your app will be live at: `https://your-app.vercel.app`

---

## ✅ Step 4: Verify Deployment

### Test Backend:
```powershell
# Check API docs
curl https://sure-financial-backend.onrender.com/docs

# Test extraction
curl -X POST https://sure-financial-backend.onrender.com/extract -F "file=@test_statement.pdf"
```

### Test Frontend:
1. Open `https://your-app.vercel.app` in browser
2. Go to Upload page
3. Upload PDF statement
4. Verify extraction works

---

## 📝 Step 5: Update README

Add these lines to your README:

```markdown
## 🚀 Live Demo

- **Frontend**: https://your-app.vercel.app
- **Backend API**: https://sure-financial-backend.onrender.com
- **API Docs**: https://sure-financial-backend.onrender.com/docs
```

---

## 🔄 Future Updates

To deploy updates after making changes:

```powershell
# Stage changes
git add .

# Commit
git commit -m "Your commit message"

# Push (auto-deploys to Render & Vercel)
git push origin main
```

Both Render and Vercel will **automatically redeploy** when you push to GitHub!

---

## 📊 Deployment Checklist

- [ ] `.gitignore` created
- [ ] Code pushed to GitHub
- [ ] Backend deployed to Render
- [ ] Backend URL copied
- [ ] Frontend deployed to Vercel
- [ ] `NEXT_PUBLIC_API_URL` added to Vercel
- [ ] Backend tested (visit `/docs`)
- [ ] Frontend tested (upload PDF)
- [ ] README updated with live URLs

---

**🎉 That's it! Your app is live!**

For detailed troubleshooting, see `DEPLOYMENT.md`.
