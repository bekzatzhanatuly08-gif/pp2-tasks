CREATE OR REPLACE PROCEDURE insert_many_contacts(
    p_names TEXT[],
    p_phones TEXT[],
    INOUT p_invalid_data TEXT[] DEFAULT '{}'
)
LANGUAGE plpgsql
AS $$
DECLARE
    i INT;
BEGIN
    IF array_length(p_names, 1) IS DISTINCT FROM array_length(p_phones, 1) THEN
        RAISE EXCEPTION 'Arrays must have same length';
    END IF;

    FOR i IN 1..array_length(p_names, 1) LOOP

        
        IF p_phones[i] ~ '^[0-9+\\-]{10,20}$' THEN

            IF EXISTS (SELECT 1 FROM phonebook WHERE name = p_names[i]) THEN
                UPDATE phonebook
                SET phone = p_phones[i]
                WHERE name = p_names[i];
            ELSE
                INSERT INTO phonebook(name, phone)
                VALUES (p_names[i], p_phones[i]);
            END IF;

        ELSE
            p_invalid_data := array_append(
                p_invalid_data,
                p_names[i] || ':' || p_phones[i]
            );
        END IF;

    END LOOP;
END;
$$;