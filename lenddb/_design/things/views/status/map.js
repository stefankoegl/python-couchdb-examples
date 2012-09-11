function(doc)
{
    if(doc.doc_type == "Thing")
    {
        emit([doc.owner, doc._id, 1], doc.name);
    }
    if(doc.doc_type == "Lending")
    {
        if(doc.lent && !doc.returned)
        {
            emit([doc.owner, doc.thing, 2], [doc.to_user, doc.lent]);
        }
    }
}
