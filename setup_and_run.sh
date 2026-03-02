#!/bin/bash
set -e
# إنشاء البيئة الافتراضية إذا لم تكن موجودة
if [ ! -d "venv" ]; then
    echo "⚡ إنشاء البيئة الافتراضية..."
    python3 -m venv venv
fi
# تفعيل البيئة
echo "🔄 تفعيل البيئة الافتراضية..."
source venv/bin/activate
# تثبيت المكتبات
echo "📦 تثبيت المكتبات..."
pip install --upgrade pip
pip install -r requirements.txt
# التحقق من المتغيرات
if [ -z "$TELEGRAM_BOT_TOKEN" ] || [ -z "$TELEGRAM_CHAT_ID" ]; then
    echo "❌ يجب تعيين TELEGRAM_BOT_TOKEN و TELEGRAM_CHAT_ID"
    echo "مثال:"
    echo "export TELEGRAM_BOT_TOKEN='توكنك'"
    echo "export TELEGRAM_CHAT_ID='ايديك'"
    exit 1
fi
# تشغيل البوت
echo "🚀 تشغيل البوت..."
./run.sh
