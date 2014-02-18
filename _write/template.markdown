---
layout: post
title:  "{{stock.Ticker}}"
date:   {{timestamp}}
categories: 观点
---

# 简介
{{stock.Ticker}}（{{stock.Company}}）是{{stock.Country}}著名上市公司，
公司主要从事{{stock.Industry}}行业，当前市值{{stock['Market Cap']}}百万美元。

# 市场表现

![{{stock.Ticker}}](http://finviz.com/chart.ashx?t={{stock.Ticker}}&ty=c&ta=1&p=d&s=l)

{{stock.Ticker}} 昨日收盘价 ${{stock.Price}}，
{% if stock.Volume > 1.2 * stock['Average Volume'] %}
交易量较正常情况有所放大。
{% elif stock.Volume > 0.8 *stock['Average Volume'] %}、
交易量有所萎缩。
{% else %}
交易保持平稳。
{% endif%}
{% if stock['20day'] > 1 %}
目前股价处于20日均线以上，
{% elif stock['20day'] < -1 %}
目前股价处于20日均线以下，
{% else %}
目前股价接近20日均线，
{% endif%}
{% if stock['50day'] > 1 %}
50日均线以上，
{% elif stock['50day'] < -1 %}
50日均线以下，
{% else %}
接近50日均线，
{% endif%}
{% if stock['200day'] > 1 %}
并且处于200日均线以上。
{% elif stock['200day'] < -1 %}
并且处于200日均线以下。
{% else %}
并且接近200日均线。
{% endif%}
从短期市场走势来看，
{% if stock['Relative Strength Index (14)'] > 70 %}
投资者应当考虑超买的风险。
{% elif stock['Relative Strength Index (14)'] < 30 %}
该股票已经超卖，投资者应当谨慎关注。
{% else %}
股价走势平稳，投资者应减少无谓的操作。
{% endif%}
{% if stock['Short Ratio'] > 40 %}
该股票空方势力强大，已经有可观比例的股票被投资者卖空。
在认识到市场悲观气氛的同时，短期内的也要留意逼空行情的出现。
{% endif%}

# 公司分析
{{stock.Ticker}} 目前静态市盈率为{{stock['P/E']}}, 动态市盈率为{{stock['Forward P/E']}}，每股收益{{stock['EPS (ttm)']}}美元,
{% if stock['Forward P/E'] > 50 %}
市场对其估值较高。
{% elif stock['Forward P/E'] < 10 %}
市场对其估值较为保守。
{% else %}
市场估值较为合理。
{% endif%}

