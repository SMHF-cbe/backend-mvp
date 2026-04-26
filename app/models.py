from __future__ import annotations

from sqlalchemy import Column, Integer, String, Float, Boolean, Date, DateTime
from datetime import date, datetime
from .database import Base


class Route(Base):
    __tablename__ = "routes"

    id = Column(Integer, primary_key=True, index=True)
    # Business route number (e.g. 1 in "Route 1 – Area Name"); unique; Excel route_id refers to this.
    route_code = Column(Integer, unique=True, nullable=True, index=True)
    name = Column(String, nullable=False)
    password = Column(String, nullable=False)


class Store(Base):
    __tablename__ = "stores"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    area = Column(String)

    price = Column(Float, nullable=False)
    route_id = Column(Integer)

    is_active = Column(Boolean, default=True)

    # Offers
    offer_type = Column(String, default="none")
    offer_buy = Column(Integer, default=0)
    offer_get = Column(Integer, default=0)
    offer_min_qty = Column(Integer, default=0)
    bundle_price = Column(Float, default=0)

    # Info
    photo_url = Column(String)
    location_url = Column(String)
    notes = Column(String)

    # Amount already owed before first tracked visit (legacy / carry-over due)
    opening_balance = Column(Float, default=0)


class Entry(Base):
    __tablename__ = "entries"

    id = Column(Integer, primary_key=True, index=True)

    date = Column(Date, default=date.today)
    created_at = Column(DateTime, default=datetime.utcnow)

    store_id = Column(Integer)
    route_id = Column(Integer)

    delivered = Column(Integer, default=0)
    returned = Column(Integer, default=0)

    free = Column(Integer, default=0)
    billable = Column(Integer, default=0)

    total_amount = Column(Float, default=0)

    amount_collected = Column(Float, default=0)
    collected_cash = Column(Float, default=0)
    collected_upi = Column(Float, default=0)
    payment_mode = Column(String)
    upi_received = Column(Boolean, default=False)

    balance = Column(Float, default=0)

    is_closed = Column(Boolean, default=False)