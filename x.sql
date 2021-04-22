   
IN_USR_ID           VARCHAR2,
IN_DVIC_ID          VARCHAR2,
IN_HSP_TP_CD        VARCHAR2,
IN_BC_YN            VARCHAR2,
DIRECT_YN           VARCHAR2,
IN_DENTAL_YN        VARCHAR2,
IN_MPD_YN           VARCHAR2,
V_SRCH_CNTE   VARCHAR2 (4000);
EMP_YN        VARCHAR2 (400);
==========================================================

      BEGIN
         SELECT COUNT (*)
           INTO EMP_YN
           FROM XBIL.PCTPCPQDV
          WHERE     PME_CLS_CD IN ('03', '01', '07')
                AND APY_STR_DT <= SYSDATE
                AND APY_END_DT >= SYSDATE
                --   and  IN_LCL_TP_CD <>'C'
                AND (TRO_NM <> '44' OR TRO_NM IS NULL)
                AND STF_CARD_NO IS NOT NULL
                AND pt_no = IN_USR_ID
                AND hsp_tp_Cd = IN_HSP_TP_CD
                AND hsp_tp_cd NOT IN ('00090', '00091')
                AND ROWNUM = 1;
      END;
==========================================================

      BEGIN
         IF IN_DENTAL_YN = 'Y'
         THEN
            OPEN OUT_CURSOR FOR
               SELECT DISTINCT B.*
                 FROM XBIL.HP_DEPARTMENTV A,
                      XBIL.HP_SERVICEV_MPD B,
                      XBIL.ACDPCACEV C
                WHERE     1 = 1
                      AND A.MED_DEPT_CD = B.MED_DEPT_CD
                      --       AND C.MED_DEPT_CD = A.MED_DEPT_CD
                      AND C.MED_SRV_CD = B.MED_SRV_CD
                      AND C.HSP_TP_CD = B.HSP_TP_CD
                      --     AND B.MP_YN = 'Y'
                      --     AND B.MP_YN = A.MP_YN
                      AND B.HSP_TP_CD = IN_HSP_TP_CD
                      AND C.USE_YN = 'Y'
                      AND B.PRTL_YN = 'Y'
                      AND B.MED_DEPT_NM LIKE '%Dent%'
                      AND C.PSE_CLS_CD IN
                             (SELECT PSE_CLS_CD
                                FROM XBIL.PCTPCPQDV
                               WHERE     PME_CLS_CD <> '14'
                                     AND APY_STR_DT <= SYSDATE
                                     AND APY_END_DT >= SYSDATE
                                     AND HSP_TP_CD = IN_HSP_TP_CD
                                     AND pt_no = IN_USR_ID);
         ELSE
            IF EMP_YN = '1'
            THEN
==========================================================
               OPEN OUT_CURSOR FOR
                    SELECT *
                      FROM (SELECT DISTINCT B.*
                              FROM XBIL.HP_DEPARTMENTV A,
                                   XBIL.HP_SERVICEV_MPD B,
                                   XBIL.ACDPCACEV C
                             WHERE     1 = 1
                                   AND A.MED_DEPT_CD = B.MED_DEPT_CD
                                   --     AND C.MED_DEPT_CD = A.MED_DEPT_CD
                                   AND C.MED_SRV_CD NOT IN ('10958', '10952' , '10959'  , '10964' , '82441' , '10970' , '10968' , '10974') --Exclude Covid19 Clinic
                                   AND C.MED_SRV_CD = B.MED_SRV_CD
                                   AND C.HSP_TP_CD = B.HSP_TP_CD
                                   --   AND B.MP_YN = 'Y'
                                   --   AND B.MP_YN = A.MP_YN
                                   AND B.HSP_TP_CD = IN_HSP_TP_CD
                                   AND C.USE_YN = 'Y'
                                   AND B.PRTL_YN = 'Y'
                                   AND B.MED_DEPT_NM NOT LIKE '%Dent%'
                                   AND C.PSE_CLS_CD IN
                                          (SELECT PSE_CLS_CD
                                             FROM XBIL.PCTPCPQDV
                                            WHERE     PME_CLS_CD <> '14'
                                                  AND APY_STR_DT <= SYSDATE
                                                  AND APY_END_DT >= SYSDATE
                                                  AND HSP_TP_CD = IN_HSP_TP_CD
                                                  AND pt_no = IN_USR_ID)
                            UNION ALL
                            SELECT DISTINCT B.*
                              FROM                   -- XBIL.HP_DEPARTMENTV A,
                                  XBIL.HP_SERVICEV_PS B, XBIL.ACDPCACEV C
                             WHERE     1 = 1
                                   -- AND A.MED_DEPT_CD = B.MED_DEPT_CD
                                   --      AND C.MED_DEPT_CD = A.MED_DEPT_CD
                                   AND C.MED_SRV_CD = B.MED_SRV_CD
                                   AND C.MED_SRV_CD NOT IN ('10958', '10952' , '10959' , '10964' , '82441' , '10970' , '10968' , '10974') --Exclude Covid19 Clinic
                                   AND C.HSP_TP_CD = B.HSP_TP_CD
                                   --    AND B.PS_YN = 'Y'
                                   --     AND B.PS_YN = A.PS_YN
                                   AND B.HSP_TP_CD = IN_HSP_TP_CD
                                   AND C.USE_YN = 'Y'
                                   AND B.PRTL_YN = 'Y'
                                   --  AND B.HSPI_TP_CD = '01'
                                   AND C.PSE_CLS_CD IN
                                          (SELECT PSE_CLS_CD
                                             FROM XBIL.PCTPCPQDV
                                            WHERE     PME_CLS_CD IN
                                                         ('03', '01', '07')
                                                  AND STF_CARD_NO IS NOT NULL
                                                  AND APY_STR_DT <= SYSDATE
                                                  AND APY_END_DT >= SYSDATE
                                                  AND HSP_TP_CD = IN_HSP_TP_CD
                                                  AND pt_no = IN_USR_ID))
                  ORDER BY LCL_SRV_NM ASC;
            ELSE
====================================================
               OPEN OUT_CURSOR FOR
                    SELECT DISTINCT B.*
                      FROM XBIL.HP_DEPARTMENTV A,
                           XBIL.HP_SERVICEV_MPD B,
                           XBIL.ACDPCACEV C
                     WHERE     1 = 1
                           AND A.MED_DEPT_CD = B.MED_DEPT_CD
                          -- AND C.MED_SRV_CD <> '10952'
                            AND C.MED_SRV_CD NOT IN ('10958', '10952' , '10959' , '10964' , '82441' , '10970' , '10968' , '10974') --Exclude Covid19 Clinic
                           --     AND C.MED_DEPT_CD = A.MED_DEPT_CD
                           AND C.MED_SRV_CD = B.MED_SRV_CD
                           AND C.HSP_TP_CD = B.HSP_TP_CD
                           --   AND B.MP_YN = 'Y'
                           --   AND B.MP_YN = A.MP_YN
                           AND B.HSP_TP_CD = IN_HSP_TP_CD
                           AND C.USE_YN = 'Y'
                           AND B.PRTL_YN = 'Y'
                           AND B.MED_DEPT_NM NOT LIKE '%Dent%'
                           AND C.PSE_CLS_CD IN
                                  (SELECT PSE_CLS_CD
                                     FROM XBIL.PCTPCPQDV
                                    WHERE     PME_CLS_CD <> '14'
                                          AND APY_STR_DT <= SYSDATE
                                          AND APY_END_DT >= SYSDATE
                                          AND HSP_TP_CD = IN_HSP_TP_CD
                                          AND pt_no = IN_USR_ID)
                  ORDER BY B.LCL_SRV_NM ASC;
