function(doc, req)
{
    return (doc.owner == req.query.friend);
}
