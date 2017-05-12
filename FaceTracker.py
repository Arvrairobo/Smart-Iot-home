import urllib
import urllib2
import json
import os.path
import ConfigParser
import MySQLdb
import sys
global config
config=ConfigParser.RawConfigParser()


def post_request(vals, url):
    """
    Build a post request.

    Args:
        vals: Dictionary of (field, values) for the POST
            request.
        url: URL to send the data to.

    Returns:
        Dictionary of JSON response or error info.
    """
    # Build the request and send to server
    data = urllib.urlencode(vals)
    encoding = "utf-8"
    on_error = "replace"
    db = MySQLdb.connect(host="127.0.0.1", user="root", passwd="sag1", db='mysql', charset='utf8', use_unicode=True)
    cursor = db.cursor()
    sql = "SELECT * FROM `facetbl`"

    try:

        cursor.execute(sql)
        for i, row in enumerate(cursor):
            try:
                # encode unicode data to the desired output encoding
                host = row[0].encode(encoding, on_error)
                user = row[1].encode(encoding, on_error)
                password = row[2].encode(encoding, on_error)
            except UnicodeEncodeError as e:
                # only if on_error='strict'
                print >> sys.stderr, "failed to encode row #%s - %s" % (i, e)
            else:
                print "Server_name=%s\nusername=%s\npassword=%s\n\n" % (host, user, password)
    finally:
        cursor.close()
        db.close()
    try:
        request = urllib2.Request(url, data)
        response = urllib2.urlopen(request)
        the_page = response.read(2000)
        print the_page
    except urllib2.HTTPError, err:
        return {"error": err.reason, "error_code": err.code}
    except:
        return {"error": "Error in connecting to server."}
    # Return the response parsed as a array from json
    try:
        return json.loads(response.read())
    except ValueError, err:
        print err
        return {"error": "JSON decoding error"}

def send_face_info(host, user, password):
    print "being called", host, user, password
    host = host
    user = user
    password = password
    cfg_path = '/home/kush/FaceTrack/FaceTrace.cfg'
    check = os.path.exists(cfg_path)
    if check == True:
        config.read(cfg_path)
        url = config.get('Settings', 'http://www.facetrack.com/post?')

    values = {'name': host,
              'user': user,
              'pass': password,
              }

    return post_request(values, url + 'host=host&user=user&password=pass')

