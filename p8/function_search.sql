CREATE OR REPLACE FUNCTION search_phonebook(p_pattern TEXT)
RETURNS TABLE(id INT, name VARCHAR, phone VARCHAR)
AS $$
BEGIN
    RETURN QUERY
    SELECT p.id, p.name, p.phone
    FROM phonebook p
    WHERE p.name ILIKE '%' || p_pattern || '%'
       OR p.phone ILIKE '%' || p_pattern || '%';
END;
$$ LANGUAGE plpgsql;