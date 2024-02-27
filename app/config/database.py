from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv


import os
#config .env
load_dotenv()

# SQLALCHEMY_DATABASE_URL = "postgresql://citizix_user:S3cret@localhost:5000/test_db"
SQLALCHEMY_DATABASE_URL = os.getenv('SQLALCHEMY_DATABASE_URL')

print("env" , SQLALCHEMY_DATABASE_URL)

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Test sorgusu yapmak için bir Session oluştur
test_session = SessionLocal()

try:
    # Bağlantıyı kontrol etmek için basit bir test sorgusu yap
    test_result = test_session.execute("SELECT 1")
    print("DB bağlantısı başarılı!")

    # Tabloları oluştur
    Base.metadata.create_all(bind=engine)
    print("Tablolar başarıyla oluşturuldu.")
except Exception as e:
    print("DB bağlantısı veya tablo oluşturma işlemi sırasında bir hata oluştu:", e)
finally:
    # Test sorgusu için açılan Session'ı kapat
    test_session.close()