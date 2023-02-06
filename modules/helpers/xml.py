namespaces = {
    "cp": "http://schemas.openxmlformats.org/package/2006/metadata/core-properties",
    "dc": "http://purl.org/dc/elements/1.1/",
    "dcterms": "http://purl.org/dc/terms/",
    "dcmitype": "http://purl.org/dc/dcmitype/",
    "xsi": "http://www.w3.org/2001/XMLSchema-instance",
    "vt": "http://schemas.openxmlformats.org/officeDocument/2006/docPropsVTypes",
    "": "http://schemas.openxmlformats.org/officeDocument/2006/extended-properties"
}


def get_value(parsed, name):
    return str(parsed.findall(name, namespaces)[0].text) \
        if parsed.findall(name, namespaces) else None


def set_value(parsed, name, value):
    if value:
        parsed.findall(name, namespaces)[0].text = str(value)
    else:
        parsed.findall(name, namespaces)[0].getparent().remove(parsed.findall(name, namespaces)[0]) \
            if parsed.findall(name, namespaces) else None
