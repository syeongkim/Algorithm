-- 코드를 입력하세요
SELECT CONCAT ('/home/grep/src/', B.BOARD_ID, '/', FILE_ID, FILE_NAME, FILE_EXT) as FILE_PATH
FROM USED_GOODS_BOARD AS A
LEFT JOIN USED_GOODS_FILE AS B
ON A.BOARD_ID = B.BOARD_ID
WHERE VIEWS = (SELECT MAX(VIEWS) FROM USED_GOODS_BOARD)
ORDER BY FILE_ID DESC