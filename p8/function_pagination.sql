CREATE OR REPLACE FUNCTION get_contacts_paginated(
    p_limit INT,
    p_offset INT
)
RETURNS TABLE(id INT, name VARCHAR, phone VARCHAR)
AS $$
BEGIN
    RETURN QUERY
    SELECT *
    FROM phonebook
    LIMIT p_limit OFFSET p_offset;
END;
$$ LANGUAGE plpgsql;