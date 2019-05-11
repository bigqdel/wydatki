<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0" 
    xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
    <xsl:template match="/">
        <html>
            <body>
                <h2>Wydatki</h2>
                
                    
                    <xsl:for-each select="Wydatki/Wydatek">
                        <ul style="list-style-type:none;">
                            <h1>Data Dodania:
                                <xsl:value-of select="DataDodania"/>
                            </h1>
                            <li>Rodzaj:
                                <xsl:value-of select="Rachunek"/>
                            </li>
                            <li>Za co:
                                <xsl:value-of select="Kategoria"/>
                            </li>
                            <li>
                                <xsl:value-of select="Waluta"/>
                            </li>
                            <li>Kwota: 
                                <xsl:value-of select="Kwota"/>
                            </li>
                            <li>Data:
                                <xsl:value-of select="Data"/>
                            </li>
                            <li>
                               
								<img width="80" height="80">
								<xsl:attribute name="src" >
								<xsl:value-of select="Plik"/>
								</xsl:attribute> 
								 
								</img>
                            </li>

                        </ul>
                    </xsl:for-each>
					<table style="color:orange; font-size:12; background-color:white;font-family:verdana;" border="1">
					<tr >
						
						
						<td style ="color:black;"> Suma Rachunków za jedzenie  </td>
						<td><xsl:value-of select="sum(//Kwota[../Kategoria='Jedzenie'])"/></td>
						<tr>
							
														<td style ="color:green;"> Suma  </td>
						<td><xsl:value-of select="sum(//Kwota)"/></td>
								
						
						</tr>
						
						
					</tr>
					</table>
                
            </body>
        </html>
    </xsl:template>

</xsl:stylesheet>
