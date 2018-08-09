
import os, inspect
from flask import render_template, jsonify
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy import create_engine, desc

from bbbioboard import app


CURR_DIR = os.path.dirname(inspect.getabsfile(inspect.currentframe()))
ROOT_DIR = os.path.dirname(CURR_DIR)

# create sqlite engine and connect to data base
fname = os.path.join(ROOT_DIR, "bbbioboard", "data", "ext", "bellybutton.sqlite")
engine = create_engine(f"sqlite:///{fname}")
Base = declarative_base(engine)


# reflect the database
class samplesTable(Base):
    __tablename__ = "samples"
    __table_args__ = {"autoload": True}
    __mapper_args__ = {'column_prefix':'bb_'}


class samplesMetaDataTable(Base):
    __tablename__ = "sample_metadata"
    __table_args__ = {"autoload": True}


# create session
session = scoped_session(sessionmaker(bind=engine))


# home route
@app.route("/home")
@app.route("/")
def home():
    return render_template("index.html")


@app.route("/names")
def names():
    bb_names = samplesTable.__table__.columns.keys()[2:]
    return jsonify(["{:04d}".format(int(elem)) for elem in bb_names])


@app.route("/samples/<bb_query>")
def get_topn_otu_values(bb_query):

    topn = 10
    sel = [samplesTable.bb_otu_id,
           samplesTable.bb_otu_label,
           getattr(samplesTable, bb_query)]

    query = session.query(*sel) \
        .filter(getattr(samplesTable, bb_query)) \
        .order_by(desc(getattr(samplesTable, bb_query))) \
        .all()[0:topn]
    d = {"id": [], "label": [], "value": []}
    list(map(lambda x: (d["id"].append("{:04d}".format(x[0])),
                        d["label"].append(x[1]),
                        d["value"].append(x[2])),
             query))

    return jsonify(d)


@app.route("/metadata/<bb_query>")
def get_metadata(bb_query):
    bb_query_number = int(bb_query.split("_")[1])
    sel = [samplesMetaDataTable.BBTYPE,
           samplesMetaDataTable.AGE,
           samplesMetaDataTable.GENDER,
           samplesMetaDataTable.CAT,
           samplesMetaDataTable.ETHNICITY,
           samplesMetaDataTable.LOCATION,
           samplesMetaDataTable.COUNTRY012,
           samplesMetaDataTable.MMAXTEMP013,
           samplesMetaDataTable.sample]
    query = session.query(*sel) \
        .filter(samplesMetaDataTable.sample == bb_query_number).first()
    d = {"type": query[0],
         "age": query[1],
         "gender": query[2],
         "category": query[3],
         "ethnicity": query[4],
         "location": query[5],
         "country": query[6],
         "temperature": query[7]}
    return jsonify([d])


@app.route("/wfreq/<bb_query>")
def get_wfreq(bb_query):
    bb_query_number = int(bb_query.split("_")[1])
    sel = [samplesMetaDataTable.WFREQ,
           samplesMetaDataTable.sample]
    query = session.query(*sel).filter(samplesMetaDataTable.sample == bb_query_number).all()

    return jsonify(query[0][0])


@app.teardown_request
def remove_session(ex=None):
    session.remove()
