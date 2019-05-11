<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0" 
    xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
    <xsl:template match="/">
        <html>
            <body>
                <h2>Wydatki</h2>
                <table border="1">
                    <tr bgcolor="#9acd32">
                        <th style="text-align:left">DataDodania</th>
                        <th style="text-align:left">Rachunek </th>
                        <th style="text-align:left">Kategoria</th>
                        <th style="text-align:left">Waluta</th>
                        <th style="text-align:left">Kwota </th>
                        <th style="text-align:left">Data</th>
                        <th style="text-align:left">Plik</th>
                    </tr>
                    <xsl:for-each select="Wydatki/Wydatek">
                        <tr>
                            <td>
                                <xsl:value-of select="DataDodania"/>
                            </td>
                            <td>
                                <xsl:value-of select="Rachunek"/>
                            </td>
                            <td>
                                <xsl:value-of select="Kategoria"/>
                            </td>
                            <td>
                                <xsl:value-of select="Waluta"/>
                            </td>
                            <td>
                                <xsl:value-of select="Kwota"/>
                            </td>
                            <td>
                                <xsl:value-of select="Data"/>
                            </td>
                            <td>
                               
								<img width="80" height="80">
								<xsl:attribute name="src" >
								<xsl:value-of select="Plik"/>
								</xsl:attribute> 
								 
								</img>
                            </td>

                        </tr>
                    </xsl:for-each>
					<tr style="color:orange; font-size:30px; background-color:powderblue;font-family:verdana;">
						<td >
							
						</td>
						<td></td>
						<td></td>
						<td style ="color:black;"> Suma  </td>
						<td >
						<xsl:value-of select="sum(//Kwota)"/></td>
						<td style ="color:black;"> PLN  </td>
						<td></td>
					</tr>
                </table>
            </body>
        </html>
    </xsl:template>

</xsl:stylesheet>